import logging
import json
from os.path import exists
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import UnitOfEnergy
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from homeassistant.util.dt import utcnow

DOMAIN = "grid_usage_tracker"
RESET_SERVICE = "reset_grid_usage"
STORAGE_PATH = "custom_components/grid_usage_tracker/grid_usage_data.json"

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities, discovery_info=None):
    sensor = GridUsageSensor(hass)
    async_add_entities([sensor], True)
    _LOGGER.info("Grid Usage Sensor added to platform")

    async def handle_reset(call):
        await sensor.async_reset_usage()
        _LOGGER.info("Grid Usage Sensor reset")

    hass.services.async_register(DOMAIN, RESET_SERVICE, handle_reset)
    _LOGGER.info("Reset service registered for Grid Usage Sensor")

class GridUsageSensor(SensorEntity):
    def __init__(self, hass: HomeAssistant):
        self._hass = hass
        self._state = 0.0
        self._attr_name = "Grid Usage"
        self._attr_unit_of_measurement = UnitOfEnergy.KILO_WATT_HOUR
        self._last_update = utcnow()

    async def async_added_to_hass(self):
        await self._load_data()
        self.async_write_ha_state()

    @property
    def name(self):
        return self._attr_name

    @property
    def state(self):
        return round(self._state, 2)

    @property
    def unit_of_measurement(self):
        return self._attr_unit_of_measurement

    async def async_update(self):
        growatt_sensor_state = self._hass.states.get("sensor.growatt_solar_grid_power")
        if growatt_sensor_state:
            power_watts = float(growatt_sensor_state.state)  # Power in watts
            now = utcnow()
            time_diff_hours = (now - self._last_update).total_seconds() / 3600.0  # Time difference in hours
            energy_kwh = (power_watts * time_diff_hours) / 1000.0  # Energy in kWh
            self._state += energy_kwh
            self._last_update = now
            await self._save_data()
            self.async_write_ha_state()

    async def async_reset_usage(self):
        self._state = 0.0
        self._last_update = utcnow()
        await self._save_data()
        self.async_write_ha_state()

    async def _load_data(self):
        if exists(STORAGE_PATH):
            data = await self._hass.async_add_executor_job(self._read_file)
            self._state = data.get('state', 0.0)
            self._last_update = utcnow()  # Reset last update time to now

    async def _save_data(self):
        rounded_state = round(self._state, 2)  # Round state to two decimal places before saving
        await self._hass.async_add_executor_job(self._write_file, {'state': rounded_state})

    def _read_file(self):
        with open(STORAGE_PATH, 'r') as file:
            return json.load(file)

    def _write_file(self, data):
        with open(STORAGE_PATH, 'w') as file:
            json.dump(data, file)
