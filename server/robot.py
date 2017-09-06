GpioEnabled = True
try:
    import RPi.GPIO as GPIO
except:
    GpioEnabled = False

# Pin constants
motorAC  = 8        # Left motor clockwise
motorACC = 10       # Left motor contraclockwise
motorBC  = 16       # Right motor clockwise
motorBCC = 18       # Right motor contraclockwise

def init():
    print("Robot: Init done")
    if GpioEnabled:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup([motorAC, motorACC, motorBC, motorBCC], GPIO.OUT, initial=GPIO.LOW)

def cleanUp():
    print("Robot: Cleanup done")
    if GpioEnabled:
        GPIO.cleanup()


def setMotors(ac, acc, bc, bcc):
    if GpioEnabled:
        GPIO.output(motorAC, ac)
        GPIO.output(motorACC, acc)
        GPIO.output(motorBC, bc)
        GPIO.output(motorBCC, bcc)

def fordwards():
    print("Robot: fordwards")
    if GpioEnabled:
        setMotors(GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW)

def backwards():
    print("Robot: backwards")
    if GpioEnabled:
        setMotors(GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH)

def right():
    print("Robot: right")
    if GpioEnabled:
        setMotors(GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.LOW)

def left():
    print("Robot: left")
    if GpioEnabled:
        setMotors(GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.LOW)

def rotateRight():
    print("Robot: rotate right")
    if GpioEnabled:
        setMotors(GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH)

def rotateLeft():
    print("Robot: rotate left")
    if GpioEnabled:
        setMotors(GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW)

def stop():
    print("Robot: stop")
    if GpioEnabled:
        setMotors(GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW)
