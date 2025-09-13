
import network
import usys
import urequests  as requests
import ujson as json
from machine import Pin, I2C
from utime import sleep
import ssd1306



#Not in use here
'''with open("/wifi_settings_openweather.json") as credentials_json:   # This pattern allows you to open and read an existing file.
    settings = json.loads(credentials_json.read())

headers = {"Content-Type": "application/json"}'''





url = "https://api.openweathermap.org/data/2.5/weather?id=1275339&units=metric&appid=40bac8a3055f133e856aa2e11aadd4ee"
#url = "https://api.openweathermap.org/data/2.5/weather?id=1275339&units=metric&appid=" + settings["open_weather_key"]   # Using location ID
#url = "https://api.openweathermap.org/data/2.5/weather?q=New York,NY,US&units=metric&appid=" + settings["open_weather_key"] # Using city, state, country




wlan = network.WLAN(network.STA_IF)     # This will create a station interface object.
                                        # To create an access point, use AP_IF (not covered here).
                                        
                                        
#Connect wifi                                        
def do_connect():
    wlan.active(True)                 # Activate the interface so you can use it.
    if not wlan.isconnected():        # Unless already connected, try to connect.
        print('connecting to network...')
        #wlan.connect(settings["wifi_name"], settings["password"])  # Connect to the station using
                                                                   # credentials from the json file.
                                                                   
        wlan.connect('LAVA LXX518', '5eyf4wyg')                                                
                                                                   
        if not wlan.isconnected():
            print("Can't connect to network with given credentials.")
            usys.exit(0)  # This will programmatically break the execution of this script and return to shell.
        print('network config:', wlan.ifconfig())


do_connect()

if wlan.isconnected() == True:
        print("Connected")
        print("My IP address: ", wlan.ifconfig()[0])  # Prints the acquired IP address
else:
    print("Not connected")





#Weather API Call
response = requests.get(url)
print("Raw response: ", response)
weather_back = json.loads(response.content)
response.close()










#Working, Need check wiring, It may cause problem
#freq also can prolem try 100000 if 400000 not working
#this is need to remember
# Try bus 1 , if 0 not working
i2c = I2C(1, scl=Pin(22), sda=Pin(21), freq=400000)
print("I2C scan:", i2c.scan())


def displayInformaion(Temperature, Humidity, Pressure, Wind):
	if 0x3C in i2c.scan():
		oled = ssd1306.SSD1306_I2C(128, 64, i2c)
		oled.fill(0)  # clear screen
		oled.text("Weather Station", 0, 0)
		oled.text("Temp: {}°C".format(Temperature), 0, 15)
		oled.text("Humidity: {}%".format(Humidity), 0, 25)
		oled.text("Press: {} hPa".format(Pressure), 0, 35)
		oled.text("Wind: {} m/s".format(Wind), 0, 45)
		oled.show()
		#sleep(10)
	else:
		print("❌ OLED not found")
    


#Display information
displayInformaion(weather_back['main']['temp'], weather_back['main']['humidity'], weather_back['main']['pressure'], weather_back['wind']['speed'])







print("------------")

for x in weather_back['weather']:
    print('The weather in %s is %s with %s.' % (weather_back["name"], x['main'], x['description']))


print('Wind is %.2f meter/sec at %s degrees.' % (weather_back['wind']['speed'], weather_back['wind']['deg']))
print('Pressure at sea level is %s hPa.' % weather_back['main']['pressure'])
print('Current conditions: Humidity %s%%, temp min %.2f°C, temp max %.2f°C.' % (weather_back['main']['humidity'], weather_back['main']['temp_min'], weather_back['main']['temp_max']))
print('Feels like %.2f°C.' % weather_back['main']['feels_like'])

print("------------")


