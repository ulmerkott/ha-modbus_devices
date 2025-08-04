# Groups

All datapoints have to be ordered in groups, where one group equals one modbus telegram/request.
When a group is read, all data from the lowest to the highest address in that group is read,
and inserted into the corresponding datapoint.

Modbus support a maximum of 125 registers in one telegram, so if your group spans a larger 
number of registers than this, the request will not be performed, and an erro thrown.

## Group definitions

All groups have to be defined before datapoints are added to them:

Parameters:

ModbusMode:		None | INPUT | HOLDING  
ModbusPollMode:	POLL_OFF | POLL_ON | POLL_ONCE

`MY_GROUP = ModbusGroup(ModbusMode.HOLDING, ModbusPollMode.POLL_ON)`

## Modbus Mode

This defines which type of registers this group contains. At the moment only input and holding registers are supported.

NONE:		Can be used if this group isn't supposed to be read  
INPUT:		Input registers  
HOLDING:	Holding registers

## Poll Mode

POLL_OFF:	Datapoints will never be polled.  
POLL_ON:	Datapoints are polled according to defined poll rate  
POLL_ONCE:	Datapoints are only polled once at startup. Can be used for values that typically don't change - serial numbers etc.

## Virtual datapoints

By setting Modbus Mode = NONE and Poll Mode = POLL_OFF, we create a group that isn't really connected to modbus.
This allows us to create datapoints (and entities) in this group that we can manipulate ourselves.
For instance, we can calculate values based on other, actually read values.
