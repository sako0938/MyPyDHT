from setuptools import setup, Extension

source_files = ['source/py_driver_wrapper.c', 'source/MyDHT_RPi_Driver/dht_driver.c', \
'source/MyDHT_RPi_Driver/MyGPIO/my_gpio.c', 'source/MyDHT_RPi_Driver/MyGPIO/my_time_utils.c', \
'source/MyDHT_RPi_Driver/MyGPIO/my_utils.c']

setup(
    name='MyPyDHT',
    version='0.1.1dev',
    packages=['MyPyDHT'],
    license='MIT',
    author='Stefano Vettor',
#    long_description=open('README.txt').read(),
	url='https://github.com/sako0938/MyPyDHT',
    ext_modules = [Extension('MyPyDHT.dht_driver', source_files, extra_compile_args=['-std=gnu99'])]
    # resource_filename(package_or_requirement, resource_name
)



# from distutils.core import setup, Extension

# source_files = ['source/py_driver_wrapper.c', 'source/MyDHT_RPi_Driver/dht_driver.c', 'source/MyDHT_RPi_Driver/MyGPIO/my_gpio.c', 'source/MyDHT_RPi_Driver/MyGPIO/my_time_utils.c', 'source/MyDHT_RPi_Driver/MyGPIO/my_utils.c']
# setup(name          = 'MyPyDHT', 
#         version     = '0.1',  
#         author      = 'Stefano Vettor', 
#         license     = 'MIT', 
#         url         = 'https://github.com/freedom27/MyPyDHT', 
#         description = 'Library to get readings from the DHT22 and the AM2302 humidity and temperature sensors on a Raspberry Pi',
#         packages    = ['MyPyDHT'],
#         ext_modules = [Extension('MyPyDHT.dht_driver', source_files, extra_compile_args=['-std=gnu99'])])
