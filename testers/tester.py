from multiprocessing import Pool
from subprocess import call
import os
import time

def simulate(testNum, repetition):
    command = './main.py tests/testimo' + str(testNum) + '.yaml -s 200 -n ' + str(repetition)
    try:
        retcode = call(command, shell=True)
    except OSError as e:
        print("Failed:", e, file=sys.stderr)

class Tester:
    def __init__(self, testNum):
        self.testNum = testNum

    def run(self):
        p = Pool(5)
        p.starmap(simulate, [(self.testNum, 1), (self.testNum, 2), (self.testNum, 3), (self.testNum, 4), (self.testNum, 5)])
        
