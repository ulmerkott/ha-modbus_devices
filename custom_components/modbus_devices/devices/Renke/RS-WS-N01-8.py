import logging

from ..modbusdevice import ModbusDevice
from ..datatypes import ModbusDatapoint, ModbusGroup, ModbusMode, ModbusPollMode
from ..datatypes import ModbusSensorData

from copy import deepcopy

from homeassistant.const import UnitOfTemperature
from homeassistant.const import PERCENTAGE
from homeassistant.components.sensor import SensorDeviceClass

_LOGGER = logging.getLogger(__name__)

class Device(ModbusDevice):
    Datapoints = deepcopy(ModbusDevice.Datapoints)

    # Override static device information
    manufacturer="Shandong Renke"
    model="RS-WS-N01-8"

    # Define groups
    GROUP_SENSORS = ModbusGroup(ModbusMode.INPUT, ModbusPollMode.POLL_ON)

    # SENSORS - Read-only
    Datapoints[GROUP_SENSORS] = {
        "Humidity": ModbusDatapoint(Address=0, Scaling=0.1, DataType=ModbusSensorData(deviceClass=SensorDeviceClass.HUMIDITY, units=PERCENTAGE)),
        "Temperature": ModbusDatapoint(Address=1, Scaling=0.1, DataType=ModbusSensorData(deviceClass=SensorDeviceClass.TEMPERATURE, units=UnitOfTemperature.CELSIUS)),
    }

    _LOGGER.debug("Loaded datapoints for %s %s", manufacturer, model)