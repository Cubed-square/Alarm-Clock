from time import sleep
On = True
#Time increment:
def count(timeH, timeM, timeS):
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
        print(f"{timeH}:{timeM}:{timeS}")
        sleep(1)
