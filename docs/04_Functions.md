# Availiable functions

There are several functions that the device class can use / override.

## onBeforeRead

This function is called every poll cycle, before the data is actually polled.

## onAfterRead

This function is called every poll cycle, after the data is actually polled.
This can be useful if you want to calculate some other data that depends on the polled data.

## onAfterFirstRead

This is called only once, after the datapoints have been read the first time, but before
the entities are created. This allows you to set up datapoints depending on the values of other datapoints.