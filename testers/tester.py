from multiprocessing import Pool
from subprocess import call
import os
import time
import platform

def simulate(testNum, repetition):
    if platform.system() == 'Linux':
        runFile = "./main.py"
    else:
        runFile = "python main.py"

    if testNum == 1:
        command = runFile + ' tests/testimo1.yaml -s 800 -n ' + str(repetition)
    elif testNum == 4:
        command = runFile + ' tests/testimo4.yaml -s 800 -n ' + str(repetition)
    elif testNum == 6:
        command = runFile + ' tests/testimo6.yaml -s 200 -n ' + str(repetition)
    elif testNum == 8:
        command = runFile + ' tests/testimo8p100.yaml -s 200 -n ' + str(repetition)
    elif testNum == 10:
        command = runFile + ' tests/testimo10.yaml -s 200 -n ' + str(repetition)
    else:
        command = 'ls'

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
        return True
        """if floatstartPosition < epsilon and (endPosition - 40) < epsilon and (endPosition - nextToLastPosition) < epsilon:
            return True
        else:
            return False"""
        

class Tester:
    def __init__(self, testNum, numOfRepetitions):
        self.testNum = testNum
        self.numOfRepetitions = numOfRepetitions
    
    def run(self):
        self.sim()
        return self.check()

    def sim(self):
        p = Pool(self.numOfRepetitions)
        if self.numOfRepetitions == 1:
            p.starmap(simulate, [(self.testNum, 1)]) 
        elif self.numOfRepetitions == 2:
            p.starmap(simulate, [(self.testNum, 1), (self.testNum, 2)])
        elif self.numOfRepetitions == 3:
            p.starmap(simulate, [(self.testNum, 1), (self.testNum, 2), (self.testNum, 3)])
        elif self.numOfRepetitions == 4:
            p.starmap(simulate, [(self.testNum, 1), (self.testNum, 2), (self.testNum, 3), (self.testNum, 4)])
        elif self.numOfRepetitions == 5:
            p.starmap(simulate, [(self.testNum, 1), (self.testNum, 2), (self.testNum, 3), (self.testNum, 4), (self.testNum, 5)])

    def check(self):
        p = Pool(self.numOfRepetitions)
        if self.numOfRepetitions == 1:
            return p.starmap(checkResults, [(self.testNum, 1)]) 
        elif self.numOfRepetitions == 2:
            return p.starmap(checkResults, [(self.testNum, 1), (self.testNum, 2)])
        elif self.numOfRepetitions == 3:
            return p.starmap(checkResults, [(self.testNum, 1), (self.testNum, 2), (self.testNum, 3)])
        elif self.numOfRepetitions == 4:
            return p.starmap(checkResults, [(self.testNum, 1), (self.testNum, 2), (self.testNum, 3), (self.testNum, 4)])
        elif self.numOfRepetitions == 5:
            return p.starmap(checkResults, [(self.testNum, 1), (self.testNum, 2), (self.testNum, 3), (self.testNum, 4), (self.testNum, 5)])
