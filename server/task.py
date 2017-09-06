import subprocess
import time

headers ="""
import robot, time
# Initializations
robot.init()
"""

footers ="""
# Cleanups
robot.cleanUp()
"""


class ExecutionManager():
    filename  = "robot_code.py"
    path = "./"
    proc = None

    def runF(self, code):
        print("--Code to run--")
        code = headers + code + footers
        print(code)
        print("---------------")
        if self.proc is not None and self.proc.poll() is None:
            print("-Externminate- " + str(self.proc.pid))
            self.proc.terminate()
        python_file = open(self.path + self.filename,'w+')
        python_file.write(code)
        python_file.close()
        self.proc = subprocess.Popen(["python3", self.path + self.filename], shell=False)
        print("Executing: " + str(self.proc.pid))


    def run(code):
        eval(code)
