from machine import Pin
from time import sleep

DT_PIN = Pin(13,Pin.IN,Pin.PULL_UP)
CLK_PIN = Pin(12,Pin.IN,Pin.PULL_UP)
SW = Pin(11,Pin.IN,Pin.PULL_UP)