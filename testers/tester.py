from multiprocessing import Pool
import subprocess
import os

def simulate(testNum):
    os.system('cd ..; ./main.py tests/testimo'+str(testNum)+'.yaml -s 200')

class Tester:
    def __init__(self, testNum):
        self.testNum = testNum

    def run(self):
        p = Pool(1)
        p.map(simulate, [self.testNum])

if __name__ == '__main__':
    tester = Tester(1)
    tester.run()

    
