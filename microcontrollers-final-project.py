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
swvalue = False

hour = 1
minute = 00
second = 00

def rotary_changed(numboptions):
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
def timeset(hourset):
    global value,swvalue,previousValue, hour
    lcd.clear()
    lcd.putstr(f"Hour: {hour}")
    sleep(1)
    while True:
        rotary_changed(hourset+1)
        if value != previousValue:
            lcd.clear()
            if value == 0:
                value = 1
            lcd.putstr(f"Hour: {value}")
            sleep(0.05)
        if swvalue == True:
            if value == 0:
                value = 1
            hour = value
            print("button pressed for time circuit")
            break
    print(hour)

def startup():
    global swvalue,value
    lcd.clear()
    lcd.putstr("24-Hour")
    lcd.move_to(0,1)
    lcd.putstr("12-Hour")
    lcd.move_to(15,0)
    lcd.blink_cursor_on()
    while True:
        rotary_changed(2)
        if value == 0:
            lcd.move_to(15,0)
        elif value == 1:
            lcd.move_to(15,1)
        else:
            print("ERROR ADJUST NUMBOPTIONS")
        if swvalue == True:
            print("button pressed")
            if value == 0:
                lcd.hide_cursor()
                timeset(24)
                TFcount(hour,minute,second)
            elif value == 1:
                lcd.hide_cursor()
                timeset(12)
                TVcount(hour,minute,second)
            lcd.clear()
            break
        
    while True:
        rotary_changed()
    print("loop complete")

startup()