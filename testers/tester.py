from multiprocessing import Pool
from subprocess import call
import os
import time
import platform

def simulate(testNum, repetition, images):
    if platform.system() == 'Linux':
        runFile = "./main.py"
    else:
        runFile = "python main.py"

    if testNum == 1:
        command = runFile + ' tests/testimo1.yaml -s 800 -t 1 -n ' + str(repetition) + ' -i ' + str(images)
    elif testNum == 4:
        command = runFile + ' tests/testimo4.yaml -s 2600 -t 4 -n ' + str(repetition) + ' -i ' + str(images)
    elif testNum == 6:
        command = runFile + ' tests/testimo6.yaml -s 600 -t 6 -n ' + str(repetition) + ' -i ' + str(images)
    elif testNum == 8:
        command = runFile + ' tests/testimo8p100.yaml -s 2000 -t 80 -n ' + str(repetition) + ' -i ' + str(images)
        try:
            retcode = call(command, shell=True)
        except OSError as e:
            print("Failed:", e, file=sys.stderr)
        command = runFile + ' tests/testimo8p110.yaml -s 2000 -t 81 -n ' + str(repetition) + ' -i ' + str(images)
        try:
            retcode = call(command, shell=True)
        except OSError as e:
            print("Failed:", e, file=sys.stderr)
        command = runFile + ' tests/testimo8p150.yaml -s 2000 -t 82 -n ' + str(repetition) + ' -i ' + str(images)
        try:
            retcode = call(command, shell=True)
        except OSError as e:
            print("Failed:", e, file=sys.stderr)
        command = runFile + ' tests/testimo8p200.yaml -s 2000 -t 83 -n ' + str(repetition) + ' -i ' + str(images)      
    elif testNum == 10:
        command = runFile + ' tests/testimo10.yaml -s 2000 -t 10 -n ' + str(repetition) + ' -i ' + str(images)

    try:
        retcode = call(command, shell=True)
    except OSError as e:
        print("Failed:", e, file=sys.stderr)

def checkResults(testNum, repetition):
    if testNum == 1:
        measurements = open('tmp/measurements' + str(repetition) + '/measurements.txt', 'r')
        epsilon = 0.1
        timeLeft = float(measurements.read().split()[0])
        measurements.close()
        return abs(timeLeft - 40) < epsilon
    elif testNum == 4:
        measurements = open('tmp/measurements' + str(repetition) + '/measurements.txt', 'r')
        timeLeft = float(measurements.read().split()[0])
        measurements.close()
        return (100/timeLeft) < 1.33
    elif testNum == 6:
        measurements = open('tmp/measurements' + str(repetition) + '/measurements.txt', 'r')
        perpetrated = float(measurements.read().split()[0])
        measurements.close()
        return perpetrated == 0
    elif testNum == 8:
        previousTime = -1.0
        with open('tmp/measurements' + str(repetition) + '/measurements.txt', 'r') as measurements:
            for time in measurements:
                if float(time) <= previousTime:
                    return False
                previousTime = float(time)
        return True
    elif testNum == 10:
        return False

class Tester:
    def __init__(self, testNum, numOfRepetitions, images):
        self.testNum = testNum
        self.numOfRepetitions = numOfRepetitions
        self.images = images
    
    def run(self):
        self.sim()
        return self.check()

    def sim(self):
        p = Pool(self.numOfRepetitions)
        if self.numOfRepetitions == 1:
            p.starmap(simulate, [(self.testNum, 1, self.images)]) 
        elif self.numOfRepetitions == 2:
            p.starmap(simulate, [(self.testNum, 1, self.images), (self.testNum, 2, self.images)])
        elif self.numOfRepetitions == 3:
            p.starmap(simulate, [(self.testNum, 1, self.images), (self.testNum, 2, self.images), (self.testNum, 3, self.images)])
        elif self.numOfRepetitions == 4:
            p.starmap(simulate, [(self.testNum, 1, self.images), (self.testNum, 2, self.images), (self.testNum, 3, self.images), (self.testNum, 4, self.images)])
        elif self.numOfRepetitions == 5:
            p.starmap(simulate, [(self.testNum, 1, self.images), (self.testNum, 2, self.images), (self.testNum, 3, self.images), (self.testNum, 4, self.images), (self.testNum, 5, self.images)])

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
