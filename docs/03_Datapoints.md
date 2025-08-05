# Datapoints

Every datapoint that is created may or may not be connected to a modbus address, and it may or
may not define a corresponding DataType (Home Assistant Entity).
To create an entitiy, we pass the "DataType" argument to our ModbusDatapoint instantiation.
For an updated list of availiable entitiy types, look at modbus_devices/devices/datatypes.py

For a datapoint with no corresponding entitity, you can do this:
```
Datapoints[MY_GROUP] = {
	"DatapointName": ModbusDatapoint(Address=0)
}
```
While to create an entity:
```
Datapoints[MY_GROUP] = {
	"DatapointName": ModbusDatapoint(Address=0, DataType=ModbusXXXXXData(....))
}
```

## Datapoints parameters

Datapoints can take the following parameters:

| Parameter | Type       | Default  | Description              |
|-----------|------------|----------|--------------------------|
| Address   | int        | 0        | 0-indexed address        |
| Length    | int        | 1        | Number of registers      |
| Scaling   | float      | 1.0      | Multiplier for raw value |
| Value     | float      | 0.0      | Scaled value             |
| Attrs     | Dict       | None     | Dict for attributes      |
| DataType  | ModbusData | None     | Entitiy parameters       |
