import logging
from .CASA_R4 import GROUP_SETPOINTS, Device as BaseDevice

_LOGGER = logging.getLogger(__name__)

class Device(BaseDevice):
    # Override static device information
    manufacturer="Swegon"
    model="CASA R15"

    def loadDatapoints(self):
        super().loadDatapoints() 

        # Modify datapoints    
        self.Datapoints[GROUP_SETPOINTS]["Temperature Setpoint"].Scaling = 1