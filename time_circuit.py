from time import sleep
#Time increment:
def count(timeH, timeM, timeS):
    timeS += 1
    if timeS >= 3:
        timeS = 0
        timeM += 1
    if timeM >= 3:
        timeM = 0
        timeH += 1
    if timeH >= 2:
        timeH = 0
    print(f"{timeH}:{timeM}:{timeS}")
    sleep(1)
