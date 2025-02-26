from .CASA_R4 import Device as BaseDevice

class Device(BaseDevice):
    def __init__(self, connection_params):
        super().__init__(connection_params)

        # Override static device information
        self.manufacturer="Swegon"
        self.model="CASA R15"

        self.Datapoints[self.GROUP_SETPOINTS]["Temperature Setpoint"].Scaling = 1