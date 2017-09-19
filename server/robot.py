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
#buzz    = 12       # Right motor contraclockwise
trig     = 11
echo     = 13

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
        GPIO.setup([motorAC, motorACC, motorBC, motorBCC, trig], GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup([echo], GPIO.IN)

def cleanUp():
    mPrint("Robot: Cleanup done")
    if GpioEnabled:
        GPIO.output(trig, False)
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


# def buzzer(ms):
#     mPrint("Robot: buzz")
#     if GpioEnabled:
#         GPIO.output(buzz, GPIO.HIGH)
#         time.sleep (ms / 1000.0)
#         GPIO.output(buzz, GPIO.LOW)


def stop():
    mPrint("Robot: stop")
    if GpioEnabled:
        setMotors(GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW)


def readDistance():
    start = 0
    end = 0
    # Configura el sensor
    GPIO.output(trig, False)
    time.sleep(0.1)  # 10 microsegundos
    # Empezamos a medir
    GPIO.output(trig, True)
    time.sleep(10*10**-6) #10 microsegundos
    GPIO.output(trig, False)

    # Flanco de 0 a 1 = inicio
    while GPIO.input(echo) == GPIO.LOW:
        start = time.time()
    # Flanco de 1 a 0 = fin
    while GPIO.input(echo) == GPIO.HIGH:
        end = time.time()

    # el tiempo que devuelve time() est ^c   en segundos
    distancia = (end - start) * 343 / 2
    print ("Distancia al objeto =", str(distancia))
    return distancia

