import logging
from .CASA_R4 import Device as BaseDevice

from copy import deepcopy

_LOGGER = logging.getLogger(__name__)

class Device(BaseDevice):
    Datapoints = deepcopy(BaseDevice.Datapoints)

    # Override static device information
    manufacturer="Swegon"
    model="CASA R15"

    # Modify datapoints    
    Datapoints[BaseDevice.GROUP_SETPOINTS]["Temperature Setpoint"].Scaling = 1

    _LOGGER.debug("Loaded datapoints for %s %s", manufacturer, model)