"""
Final Project Comp 430
Developer(s): Justin Myshrall
Date: 4/6/2023
"""

import RPi.GPIO as GPIO
import time
import Adafruit_ADS1x15                 # From Adafruit library pip install `adafruit-ads1x15`

# Import necessary libraries

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1                               	 	# GAIN setting of 1x so ±4.096V for sensor
PIN = 21                               		# GPIO pin for water pump
PUMP_RUNTIME = 5                      	# Time in s pump stays on for
DAY = 86400                            	# Day is 86400 seconds
TIME_ELAPSED = DAY                  # Set interval as a day between activations
last_time = 0                           		# Initializes time at 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)               # Establishes BCM numbering system
GPIO.setup(PIN, GPIO.IN)                # Initializes as OFF

values = [0] * 100                      	# List to store `adc` readings (soil sensor)
try:
    while True:
        for i in range(100):
            values[i] = adc.read_adc(0, gain=GAIN)          # Reads values found from soil sensor
            time.sleep(0.1)
            print(max(values))                              		   # Tells user current value
        if (max(values)) > 20000:                          	   # > 20000 is dry, < is wet
            if (time.time() - last_time) >= TIME_ELAPSED:
                GPIO.setup(PIN, GPIO.OUT)                      # Turns pump on with .OUT
                print("PUMP ON")
                time.sleep(PUMP_RUNTIME)                    # Turns pump on for set time
                GPIO.setup(PIN, GPIO.IN)                    	  # Turns off after elapsed time
                print("PUMP OFF")
                last_time = time.time()
            else:
                print("Pump not turned on, day has not elapsed")
        else:
            GPIO.setup(PIN, GPIO.IN)                    	# Turns pump off with .IN
            print("PUMP OFF")
            time.sleep(0.1)
finally:
    GPIO.cleanup()                                               	# Releases pins when program exits
