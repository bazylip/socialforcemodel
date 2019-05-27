from multiprocessing import Pool
from subprocess import call
import os
import time

def simulate(testNum, repetition):
    if testNum == 1:
        command = './main.py tests/testimo' + str(testNum) + '.yaml -s 800 -n ' + str(repetition)
    elif testNum == 2:
        command = 'print "error"'
    elif testNum == 3:
        command = 'print "error"'
    elif testNum == 4:
        command = 'print "error"'
    elif testNum == 5:
        command = 'print "error"'
    else:
        command = 'print "error"'

    try:
        retcode = call(command, shell=True)
    except OSError as e:
        print("Failed:", e, file=sys.stderr)

def checkResults(testNum, repetition):
    if testNum == 1:
        measurements = open('tmp/measurements' + str(repetition) + '/measurements.txt', 'r')
        count = 1
        epsilon = 0.1
        for position in measurements.read().split():
            if count == 1:
                
                startPosition = position
            elif count == 799:
                nextToLastPosition = position
            elif count == 800:
                lastPosition = position
        
        if startPosition < epsilon and (endPosition - 40) < epsilon and (endPosition - nextToLastPosition) < epsilon:
            return True
        else:
            return False
        

class Tester:
    def __init__(self, testNum):
        self.testNum = testNum
    
    def run(self):
        self.sim()
        return self.check()

    def sim(self):
        p = Pool(5)
        p.starmap(simulate, [(self.testNum, 1), (self.testNum, 2), (self.testNum, 3), (self.testNum, 4), (self.testNum, 5)]) 

    def check(self):
        p = Pool(5)
        return p.starmap(checkResults, [(self.testNum, 1), (self.testNum, 2), (self.testNum, 3), (self.testNum, 4), (self.testNum, 5)]) 
        
