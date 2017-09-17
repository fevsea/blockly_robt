import subprocess
import time
import asyncio
import websockets
import json
import threading

headers ="""
import robot
import time
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
        codeR = self.generateFile(code)
        python_file = open(self.path + self.filename, 'w+')
        python_file.write(codeR)
        python_file.close()
        if self.proc is not None and self.proc.poll() is None:
            print("-Externminate- " + str(self.proc.pid))
            self.proc.terminate()
        self.proc = subprocess.Popen(["python3", self.path + self.filename], shell=False)
        pid = str(self.proc.pid)
        print("Executing: " + pid)
        return pid



    def generateFile(self, code):
        print("--Code to run--")
        codeOut = headers
        for line in code.splitlines():
            codeOut += "" + line + "\n"
        codeOut += footers
        print(codeOut)
        print("---------------")
        return codeOut

    def runPopen(self, code):
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
        pid = str(self.proc.pid)
        print("Executing: " + pid)
        return pid

    def run(code):
        eval(code)
