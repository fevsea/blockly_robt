
import robot, time
# Initializations
robot.init()
i = None


for i in range(1, 11):
  robot.buzzer((i * 10))time.sleep(0.2)

# Cleanups
robot.cleanUp()
