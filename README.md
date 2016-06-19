# MyPyDHT
MyPyDHT is a small library in python 3 for the Raspberry Pi (1, 2, 3 and Zero) to interact with the humidity & temperature sensors DHT11, DHT22 and AM2302.
## Installation
Before installing it be sure that your Pi is compatible with Python Extensions. On Raspbian the following commands will ensure it:
````
apt-get update
sudo apt-get install build-essential python-dev
````
Since this library use git submodels use the following command to clone the repository:
````
git clone --recursive https://github.com/freedom27/MyPyDHT
````
Once the repository has been cloned enter the following command inside the main folder:
````
sudo python setup.py install
````
Now MyPyDHT is succesfully installed and ready to be used inside your python projects!

## How to use
In any python file you whish to use the library import the module and call the sensor_read function as follow:
```python
import MyPyDHT

# if for instance you have a DHT22 sensor connected to the GPIO port 17
humidity, temperature = MyPyDHT.sensor_read(MyPyDHT.Sensor.DHT22, 17)
# humidity = 22.1 (it's a percentage), temperature = 20.3 (celsius degrees)
```
In the example above th function _sensor_read_ accept in input the BCM GPIO port to which the sensor is connected.
With just the GPIO port in input the module will try to access the sensor but in case of failure it raises a __DHTException__.

The full signature of the _sensor_read_ function is:
```python
def sensor_read(sensor_type, gpio_pin, reading_attempts=1, use_cache=False):
```
Where:
+ __sensor_type__: is an enum (the _Sensor_ enum) telling which model of DHT sensors is we are trying to read; possible values are __DHT11__ and __DHT22__
+ __gpio_pin__: the number of the port to which the sensor is connected
+ __reading_attempts__ (optional): this is the total number of attempts to read data from the sensor before returning an excaption in case of failure
+ __use_cache__ (optional): if this parameter is set to __true__ in case of failure of all the the reading attempts the function will return the last valid data retrieved from the sensor instead of raising an Exception (if sampling rate is high cached data should be accurate)

The __DHTException__ class has an attribude _message_ describing what issue occurred while attempting to read the sensor.
