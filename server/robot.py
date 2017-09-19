import json
import time
import os
GpioEnabled = True
try:
    import RPi.GPIO as GPIO
except:
    GpioEnabled = False

# Pin constants
motorAC  = 40        # Left motor clockwise
motorACC = 38       # Left motor contraclockwise
motorBC  = 16       # Right motor clockwise
motorBCC = 18       # Right motor contraclockwise
buzz     = 12       # Right motor contraclockwise

index    = 0

def mPrint(data):
    print(data)
    js = json.dumps({'op': 'PROGRAM_PRINT', 'data': data})
    files = os.listdir("out/")
    files.sort()
    filename = files[-1] if files else "0"
    global index
    index += 1
    python_file = open("out/filename" + str(index), 'w+')
    python_file.write(js)
    python_file.close()

def init():
    mPrint("Robot: Init done")
    if GpioEnabled:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup([motorAC, motorACC, motorBC, motorBCC, buzz], GPIO.OUT, initial=GPIO.LOW)

def cleanUp():
    mPrint("Robot: Cleanup done")
    if GpioEnabled:
        GPIO.cleanup()


def setMotors(ac, acc, bc, bcc):
    if GpioEnabled:
        GPIO.output(motorAC, ac)
        GPIO.output(motorACC, acc)
        GPIO.output(motorBC, bc)
        GPIO.output(motorBCC, bcc)

def fordwards():
    mPrint("Robot: fordwards")
    if GpioEnabled:
        setMotors(GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW)

def backwards():
    mPrint("Robot: backwards")
    if GpioEnabled:
        setMotors(GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH)

def right():
    mPrint("Robot: right")
    if GpioEnabled:
        setMotors(GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.LOW)

def left():
    mPrint("Robot: left")
    if GpioEnabled:
        setMotors(GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.LOW)

def rotateRight():
    mPrint("Robot: rotate right")
    if GpioEnabled:
        setMotors(GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH)

def rotateLeft():
    mPrint("Robot: rotate left")
    if GpioEnabled:
        setMotors(GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW)

def buzzer(ms):
    mPrint("Robot: buzz")
    if GpioEnabled:
        GPIO.output(buzz, GPIO.HIGH)
        time.sleep (ms / 1000.0)
        GPIO.output(buzz, GPIO.LOW)

def stop():
    mPrint("Robot: stop")
    if GpioEnabled:
        setMotors(GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW)
