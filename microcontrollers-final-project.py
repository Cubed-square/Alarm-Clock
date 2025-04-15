import utime
from utime import sleep
import machine
from machine import I2C,ADC,Pin
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
DT_Pin = Pin(13,Pin.IN,Pin.PULL_UP)
CLK_Pin = Pin(12,Pin.IN,Pin.PULL_UP)
SW = Pin(11,Pin.IN,Pin.PULL_UP)
value = 0
previousValue = 1
numboptions = 2
swvalue = False

hour = int(input("What hour is it?: "))
minute = int(input("What minute is it?: "))
second = int(input("What second is it?: "))

def rotary_changed():
    global previousValue
    global value
    global swvalue
    if previousValue != CLK_Pin.value():
        if CLK_Pin.value() == 0:
            if DT_Pin.value() == 0:
                value = (value - 1)%numboptions
                return value
            else:
                value = (value + 1)%numboptions
                return value               
        previousValue = CLK_Pin.value()
    if SW.value() == 0:       
        swvalue = True
        return swvalue

def startup():
    global swvalue
    lcd.clear()
    lcd.putstr("24-Hour")
    lcd.move_to(0,1)
    lcd.putstr("12-Hour")
    lcd.move_to(15,0)
    lcd.blink_cursor_on()
    while True:
        rotary_changed()
        if value == 0:
            lcd.move_to(15,0)
        elif value == 1:
            lcd.move_to(15,1)
        else:
            print("ERROR ADJUST NUMBOPTIONS")
        if swvalue == True:
            print("button pressed")
            lcd.clear()
            break
        
    while True:
        rotary_changed()
    print("loop complete")

startup()
'''
TFcount(hour, minute, second)
TVcount(hour, minute, second)
'''