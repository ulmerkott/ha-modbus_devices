# General info

The purpose of this integration is to allow integration of modbus devices in Home Assistant that:
* Are recognized as true "devices"
* Are easily multiplied in cases where one has multiple similar devices
* Allows manipulation and calculation of values

## Installation

Download using HACS (add repository manually) or manually download and put it in the custom_components folder.

## Usage

Create a new device file (devices/manufacturer/devicemodel.py). This file needs to define the following:
* A "Device" class subclassing ModbusDevice:
* Group definitions
* Datapoints for each of the previously defined groups

Take a look at an existing device file as an example