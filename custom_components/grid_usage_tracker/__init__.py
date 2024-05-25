import logging
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

DOMAIN = "grid_usage_tracker"

_LOGGER = logging.getLogger(__name__)

def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    _LOGGER.info("Setting up Grid Usage Tracker")
    return True
