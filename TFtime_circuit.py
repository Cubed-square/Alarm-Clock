from time import sleep
import machine
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
#I2C header
I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

On = True
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
#Time increment:
def TFcount(timeH, timeM, timeS):
    while On:
        timeS += 1
        if timeS >= 60:
            timeS = 0
            timeM += 1
        if timeM >= 60:
            timeM = 0
            timeH += 1
        if timeH >= 24:
            timeH = 0
        lcd.clear()
        lcd.putstr(f"Time: {timeH}:{timeM}:{timeS}")
        lcd.move_to(0,0)
        sleep(1)
