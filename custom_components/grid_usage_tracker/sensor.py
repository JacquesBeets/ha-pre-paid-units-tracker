import logging
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import ENERGY_KILO_WATT_HOUR

DOMAIN = "grid_usage_tracker"
RESET_SERVICE = "reset_grid_usage"

_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_entities, discovery_info=None):
    sensor = GridUsageSensor()
    add_entities([sensor])

    def handle_reset(call):
        sensor.reset_usage()

    hass.services.register(DOMAIN, RESET_SERVICE, handle_reset)

class GridUsageSensor(SensorEntity):
    def __init__(self):
        self._state = 0.0
        self._attr_name = "Grid Usage"
        self._attr_unit_of_measurement = ENERGY_KILO_WATT_HOUR

    @property
    def state(self):
        return self._state

    def update(self):
        # Update the sensor state by fetching data from the source sensor
        growatt_sensor_state = self.hass.states.get("sensor.growatt_solar_grid_power")
        if growatt_sensor_state:
            self._state += float(growatt_sensor_state.state)

    def reset_usage(self):
        self._state = 0.0
        self.async_write_ha_state()
