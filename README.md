# BME280 Project
Code to interrogate a BME280, providing ambient temperature, pressure and humidity for a few euro.
Based on 
[sample code](https://www.raspberrypi-spy.co.uk/2016/07/using-bme280-i2c-temperature-pressure-sensor-in-python)
by Matt Hawkins, last updated 21/01/2018

1. Enable I2C is the RPi settings.
2. Use 
```
i2cdetect -y 1
```
to see if the BME280 is detected. It should be on 76 or 77, you must adjust the code to match.

The image below shows a BME280 wired into a CM4 IO Board. It also shows DS18B20 based temperature sensors (dfifferent project!).

<img title="BME280 on CM4" alt="BME280" src="/images/BME280.jpg">
