from machine import Pin
from time import sleep

DT_Pin = Pin(13,Pin.IN,Pin.PULL_UP)
CLK_Pin = Pin(12,Pin.IN,Pin.PULL_UP)
SW = Pin(11,Pin.IN,Pin.PULL_UP)

value = 0
previousValue = 1
numboptions = 5


def rotary_changed():
    
    global previousValue
    global value
    
    if previousValue != CLK_Pin.value():
        if CLK_Pin.value() == 0:
            if DT_Pin.value() == 0:
          
                value = (value - 1)%numboptions
                print("anti-clockwise", value)
            else:
        
                
                value = (value + 1)%numboptions
                print("clockwise", value)                
        previousValue = CLK_Pin.value()
         
         
    if SW.value() == 0:       
        print("Button pressed") 

    


while True:
    rotary_changed()
    sleep(0.001)   
