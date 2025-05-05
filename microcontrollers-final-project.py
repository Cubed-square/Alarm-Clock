import utime
from utime import sleep
import machine
from picozero import Speaker
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
#Buzzer
speaker = Speaker(5)
BEAT = 1
#Display
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
#Rotary Encoder
DT_Pin = Pin(13,Pin.IN,Pin.PULL_UP)
CLK_Pin = Pin(12,Pin.IN,Pin.PULL_UP)
SW = Pin(11,Pin.IN,Pin.PULL_UP)
value = 0
previousValue = 1
swvalue = False
#Time
hour = 1
minute = 00
second = 00

class song:
    def stocksong():
        global BEAT
        BEAT = .25 #120 BPM
        global included
        included = [ ['d4', BEAT / 2], ['d#4', BEAT / 2], ['f4', BEAT], ['d5', BEAT], ['a#4', BEAT], ['d4', BEAT],  
                      ['f4', BEAT], ['d#4', BEAT], ['d#4', BEAT], ['c4', BEAT / 2],['d4', BEAT / 2], ['d#4', BEAT], 
                      ['c5', BEAT], ['a4', BEAT], ['d4', BEAT], ['g4', BEAT], ['f4', BEAT], ['f4', BEAT], ['d4', BEAT / 2],
                      ['d#4', BEAT / 2], ['f4', BEAT], ['g4', BEAT], ['a4', BEAT], ['a#4', BEAT], ['a4', BEAT], ['g4', BEAT],
                      ['g4', BEAT], ['', BEAT / 2], ['a#4', BEAT / 2], ['c5', BEAT / 2], ['d5', BEAT / 2], ['c5', BEAT / 2],
                      ['a#4', BEAT / 2], ['a4', BEAT / 2], ['g4', BEAT / 2], ['a4', BEAT / 2], ['a#4', BEAT / 2], ['c5', BEAT],
                      ['f4', BEAT], ['f4', BEAT], ['f4', BEAT / 2], ['d#4', BEAT / 2], ['d4', BEAT], ['f4', BEAT], ['d5', BEAT],
                      ['d5', BEAT / 2], ['c5', BEAT / 2], ['b4', BEAT], ['g4', BEAT], ['g4', BEAT], ['c5', BEAT / 2],
                      ['a#4', BEAT / 2], ['a4', BEAT], ['f4', BEAT], ['d5', BEAT], ['a4', BEAT], ['a#4', BEAT * 1.5]]
        speaker.play(included)

    def smokonwat():
        global BEAT
        BEAT = 2.088 #115 BPM
        global smokeonwater
        smokeonwater = [['g3',BEAT/4],['a#3',BEAT/4],['c4',BEAT/4],['',BEAT/8],['g3',BEAT/8],['',BEAT/8],['a#3',BEAT/4],['d#4',BEAT/8],['c4',BEAT/4]]
        speaker.play(smokeonwater)

    def polkka(): #Ab-> G#; Bb -> A#; Eb -> D#
        global BEAT
        BEAT = 1.5 #120bpm = 0.5s; 1.5 is set for wokwi sim
        sakijar = [['g4',BEAT/16],['a4',BEAT/16],['b4',BEAT/16], #MEASURE 1
        ['c5',BEAT/8],['g4',BEAT/16],['g#4',BEAT/16],['g4',BEAT/16],['f4',BEAT/8],['d#4',BEAT/8], #MEASURE 2
        ['d#4',BEAT/16],['f4',BEAT/16],['d#4',BEAT/16],['d4',BEAT/8],['d4',BEAT/16],['g3',BEAT/16],['b3',BEAT/16],['d4',BEAT/16], #MEASURE 3
        ['g4',BEAT/8],['f4',BEAT/16],['g4',BEAT/16],['f4',BEAT/16],['d#4',BEAT/8],['d4',BEAT/8], #MEASURE 4
        ['d#4',BEAT/16],['d4',BEAT/16],['c4',BEAT/8],['b3',BEAT/16],['c4',BEAT/16],['d#4',BEAT/16],['g4',BEAT/16],#MEASURE 5
        ['c5',BEAT/8],['g4',BEAT/16],['g#4',BEAT/16],['g4',BEAT/16],['f4',BEAT/8],['d#4',BEAT/8], #MEASURE 6
        ['d#4',BEAT/16],['f4',BEAT/16],['d#4',BEAT/16],['d4',BEAT/8],['d4',BEAT/16],['g3',BEAT/16],['b3',BEAT/16],['d4',BEAT/16], #MEASURE 7
        ['g4',BEAT/8],['f4',BEAT/16],['g4',BEAT/16],['f4',BEAT/16],['d#4',BEAT/8],['d4',BEAT/8], #MEASURE 8
        ['c4',BEAT/8],['',BEAT/8],['c4',BEAT/8]]
        speaker.play(sakijar)

    def megalovania():
        global BEAT
        BEAT = 2
        global megalov
        megalov = [['c3',BEAT/16],['c3',BEAT/16],['d4',BEAT/8],['a3',BEAT/8],['',BEAT/16],['g#3',BEAT/16],['',BEAT/16],
                   ['g3',BEAT/16],['',BEAT/16],['f3',BEAT/16],['f3',BEAT/16],['d3',BEAT/16],['f3',BEAT/16],['g3',BEAT/16]]
        speaker.play(megalov)

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

def MILtimeset(hourset):
    global value,swvalue,previousValue,hour,minute
    lcd.clear()
    lcd.putstr(f"Hour: {hour}")
    sleep(1)
    swvalue = False
    lcd.clear()
    lcd.putstr("Hour: ")
    while True:
        rotary_changed(24)
        lcd.move_to(5,0)
        if (value) < 10:
            lcd.putstr(f" {str(value)}")
        else:
            lcd.putstr(str(value))
        if swvalue == True:
            lcd.clear()
            lcd.putstr(f"Selected: {value}")
            hour = value
            break
    sleep(1)
    swvalue = False
    lcd.clear()
    lcd.putstr("Minute: ")
    while True:
        rotary_changed(59)
        lcd.move_to(7,0)
        if (value) < 10:
            lcd.putstr(f" {str(value)}")
        else:
            lcd.putstr(str(value))
        if swvalue == True:
            lcd.clear()
            lcd.putstr(f"Selected: {value}")
            minute = value
            break
    print(hour)
    print(minute)
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
                MILtimeset(24)
                TFcount(hour,minute,second)
            elif value == 1:
                lcd.hide_cursor()
                timeset(12)
                break
            lcd.clear()
            swvalue = False
            break

    while True:
        rotary_changed(hour)
    print("loop complete")


startup()
#speaker.play(song.megalovania())