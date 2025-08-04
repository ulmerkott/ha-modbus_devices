# Datatypes (Home Assistant Entities)

Every datapoint that is created may or may not define a corresponding Home Assistant Entity.
To create an entitiy, we pass the "DataType" argument to our ModbusDatapoint instantiation.
For an updated list of availiable entitiy types, look at modbus_devices/devices/datatypes.py

For a datapoint with no corresponding entitity, you can do this:
Datapoints[MY_GROUP] = {
	"DatapointName": ModbusDatapoint(Address=0)
}
While to create an entity:
Datapoints[MY_GROUP] = {
	"DatapointName": ModbusDatapoint(Address=0, DataType=ModbusXXXXXData(....))
}

## Common parameters

All DataTypes can take the following parameters:

deviceClass:	None | Load value from HA device class 
category:		None | "config" | "diagnostic"
icon:			None | "mdi:thermometer"

## ModbusSensorData

This creates a "Sensor" entity. Typically used for most readonly values.

Parameters:	
units:			None | "%" | SensorDeviceClass.TEMPERATURE
enum:			None | {0: "Value0", 1: "Value1", 2:"Value2"}

Datapoints[MY_GROUP] = {
	"DatapointName": ModbusDatapoint(Address=0, DataType=ModbusSensorData(deviceClass=SensorDeviceClass.TEMPERATURE, units=UnitOfTemperature.CELSIUS)),
}

## ModbusNumberData

This creates a "Number" entity. Typically used for numeric input.

Parameters:	
units:			None | "%" | NumberDeviceClass.TEMPERATURE
min_value:		0
max_value:		65535
step:			1

Datapoints[MY_GROUP] = {
	"DatapointName": ModbusDatapoint(Address=0, DataType=ModbusNumberData(deviceClass=NumberDeviceClass.TEMPERATURE, units=UnitOfTemperature, min_value=10, max_value=30, step=0.5)),
}

## ModbusSelectData

This creates a "Select" entity. This creates a dropdown/select for enumerated values.

Parameters:	
options:		{0: "Value0", 1: "Value1", 2:"Value2"}

Datapoints[MY_GROUP] = {
	"DatapointName": ModbusDatapoint(Address=0, DataType=ModbusSelectData(options={0: "Stopped", 1: "Running", 2: "Error"})),
}

## ModbusBinarySensorData

This creates a "BinarySensor" entity. Typically used to display binary values.
Use device class to get more specific texts in the UI.

This type has no specific parameters.

Datapoints[MY_GROUP] = {
	"DatapointName": ModbusDatapoint(Address=0, DataType=ModbusBinarySensorData(deviceClass=BinarySensorDeviceClass.OCCUPANCY)),
}

## ModbusSwitchData

This creates a "Switch" entity. Typically used for writable binary values.

This type has no specific parameters.

Datapoints[MY_GROUP] = {
	"DatapointName": ModbusDatapoint(Address=0, DataType=ModbusSwitchData()),
}

## ModbusButtonData

This creates a "Button" entity. A button press will set the corresponding tag.

This type has no specific parameters.

Datapoints[MY_GROUP] = {
	"DatapointName": ModbusDatapoint(Address=0, DataType=ModbusButtonData()),
}