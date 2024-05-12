#!/usr/bin/env python3

'''
bme280 tools
by: JOR 2024
Alpha version:  12MAY24
Based on code by Matt Hawkins, 21/01/2018
'''

from Source.my_bme280 import readBME280ID
from Source.my_bme280 import readBME280All

  
if __name__=="__main__":
  
  (chip_id, chip_version) = readBME280ID()
  print ("Chip ID     :", chip_id)
  print ("Version     :", chip_version)

  temperature,pressure,humidity = readBME280All()
  print ("Temperature : ", temperature, "C")
  print ("Pressure : ", pressure, "hPa")
  print ("Humidity : ", humidity, "%")


 
