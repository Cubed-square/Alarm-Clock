import utime
from utime import sleep
import machine
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from time import sleep
from TFtime_circuit import TFcount
from TVtime_circuit import TVcount

#I2C header
I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

#creating components
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
hour = int(input("What hour is it?: "))
minute = int(input("What minute is it?: "))
second = int(input("What second is it?: "))
def startup(hr, mini, sec):
    global hour, minute, second
    hour = hr
    minute = mini
    second = sec
    print("starting")
    lcd.putstr(f"Time: {hour}:{minute}:{second}")
    lcd.move_to(0,1)
    lcd.putstr("Alarm: Armed")
    lcd.move_to(0,0)
startup(hour, minute, second)

TFcount(hour, minute, second)
TVcount(hour, minute, second)