import MyPyDHT.dht_driver
import time

class DHTException(Exception):
    def __init__(self, mess):
        self.message = mess

DHT_HANDSHAKE_ERROR     = -1
DHT_TIMEOUT_ERROR       = -2
DHT_CHECKSUM_ERROR      = -3
DHT_INPUT_ERROR         = -4
DHT_INIT_ERROR          = -5
DHT_OK                  =  0

_cached_data = (0, 0)

def sensor_read(gpio_pin, reading_attempts=1, use_cache=False):
    global _cached_data
    attempts = 0
    while True:
        result, humidity, temperature = MyPyDHT.dht_driver._dht_read(gpio_pin)
        if result == DHT_OK:
            _cached_data = humidity, temperature
            break
        else:
            attempts += 1
            if attempts < reading_attempts:
                time.sleep(1)
            else:
                break
    
    if result != DHT_OK:
        if use_cache:
            humidity, temperature = _cached_data
        else:
            if result == DHT_HANDSHAKE_ERROR:
                error_mess = "An error occurred during the handshake with the sensor!"
            elif result == DHT_TIMEOUT_ERROR:
                error_mess = "A timeout occurred while attempting to read the sensor!"
            elif result == DHT_CHECKSUM_ERROR:
                error_mess = "The checksum verification of sensors' data failed!"
            elif result == DHT_INIT_ERROR:
                error_mess = "An error occurred while initializing the GPIO ports"
            else:
                #result == DHT_INPUT_ERROR
                error_mess = "Invalid data passed as arguments to the sensor!"
            raise DHTException(error_mess)
     
    return round(humidity, 2), round(temperature, 2)

