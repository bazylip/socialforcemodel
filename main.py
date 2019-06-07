#!/usr/bin/env python

import socialforcemodel as sfm
import numpy as np
import matplotlib.pyplot as plt

flagLeft = False
timeLeft = -1.0
perpetrated = 0

def imo1Leaving(world):
    epsilon = 0.001
    global timeLeft
    global flagLeft 
    for group in world.groups:
        for p in group.pedestrians:
            if abs(p.position[0] - 42) < epsilon and not flagLeft:
                flagLeft = True
                timeLeft = world.time

def imo4timeToLeaveRoom(world):
    counter = 0
    global timeLeft
    global flagLeft

    for group in world.groups:
        for p in group.pedestrians:
            if p.position[0] < 10:
                counter += 1
    
    if counter == 0 and not flagLeft:
        flagLeft = True
        timeLeft = world.time
    
def imo6perpetratingCorner(world):
    global perpetrated

    for group in world.groups:
        for p in group.pedestrians:
            if p.position[0] < 13.15 and p.position[1] > 4.85:
                perpetrated = 1
    
def imo8timeToMove(world):
    counter = 0
    global timeLeft
    global flagLeft

    for p in world.groups[0].pedestrians:
        if p.position[0] < 22:
            counter += 1
    
    if counter == 0 and not flagLeft:
        flagLeft = True
        timeLeft = world.time

def main(args):
    loader = sfm.ParameterLoader(args.file)
    world = loader.world
    world.update()
    global timeLeft
    global perpetrated


    if args.test == 1:
        world.add_measurement(imo1Leaving)
    elif args.test == 4:
        world.add_measurement(imo4timeToLeaveRoom)
    elif args.test == 6:
        world.add_measurement(imo6perpetratingCorner)
    elif args.test == 80 or args.test == 81 or args.test == 82 or args.test == 83:
        world.add_measurement(imo8timeToMove)

    figure = world.plot()
    figure.savefig("tmp/img" + str(args.number) + "/0.png",
                   bbox_inches = 'tight',
                   pad_inches = 0.1)
    figure.clear()
    plt.close(figure)

    for step in range(args.steps):
        if not world.step():
            break
        world.update()
        if step % (args.steps / args.images) == (args.steps / args.images) - 1:
            figure = world.plot()
            figure.savefig("tmp/img" + str(args.number) + "/" + str((step + 1)/(args.steps / args.images)) + ".png",
                           bbox_inches = 'tight',
                           pad_inches = 0.1)
            figure.clear()
            plt.close(figure)

    if args.test == 1 or args.test == 4 or args.test == 80:
        np.savetxt("tmp/measurements" + str(args.number) + "/measurements.txt", np.array(timeLeft).reshape(1,), fmt="%1.4f")
    elif args.test == 6:
        np.savetxt("tmp/measurements" + str(args.number) + "/measurements.txt", np.array(perpetrated).reshape(1,), fmt="%d")
    elif args.test == 81 or args.test == 82 or args.test == 83:
        f = open("tmp/measurements" + str(args.number) + "/measurements.txt", 'ab')
        np.savetxt(f, np.array(timeLeft).reshape(1,), fmt="%1.4f")
        f.close()

if __name__ == '__main__':
    import argparse
    import sys
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='YAML-file')
    parser.add_argument('-s', '--steps', help='Number of steps', type=int, default=500)
    parser.add_argument('-t', '--test', help='Number of test', type=int)
    parser.add_argument('-n', '--number', help='Number of repetition (1,2,3,4,5)', type=int)
    parser.add_argument('-i', '--images', help='Number of images', type=int)
    args = parser.parse_args(sys.argv[1:])
    main(args)
