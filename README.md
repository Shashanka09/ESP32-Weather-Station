# ESP32 Weather Station with OLED Display  

This project connects an ESP32 microcontroller to Wi-Fi, retrieves live weather data from the [OpenWeather API](https://openweathermap.org/api), and displays key parameters — temperature (°C), humidity (%), pressure (hPa), and wind speed (m/s) — on a 128×64 SSD1306 OLED display over I²C.

---

## ✨ Features  

- Connects ESP32 to Wi-Fi using MicroPython’s `network` module.  
- Fetches live weather data from OpenWeather API using `urequests`.  
- Parses JSON responses with `ujson`.  
- Displays temperature, humidity, pressure, and wind speed on SSD1306 OLED over I²C.  
- Uses formatted text and the °C symbol for clear display.  

---

## 🛠️ Hardware Required  

- ESP32 board  
- SSD1306 128×64 OLED display (I²C)  
- Jumper wires  
- USB cable for flashing MicroPython  

---

## ⚡ Circuit Diagram  

| ESP32 Pin | SSD1306 Pin |
|-----------|-------------|
| 3.3V      | VCC         |
| GND       | GND         |
| GPIO 22   | SCL         |
| GPIO 21   | SDA         |

---------

## 📂 Installation  

1. **Flash MicroPython** firmware onto your ESP32 (download from [micropython.org](https://micropython.org/download/esp32/)).  
2. Use [Thonny IDE](https://thonny.org/) or [uPyCraft](https://randomnerdtutorials.com/install-uPyCraft-ide-windows/) to upload the `.py` file to the ESP32.  
3. Replace Wi-Fi SSID, password, and your OpenWeather API key in the script.  

---

## ▶️ Usage  

1. Power up the ESP32.  
2. The script will connect to Wi-Fi.  
3. Weather data will be fetched and displayed on the OLED automatically.  
4. Open the MicroPython REPL to view debug prints like raw API responses.  

---

