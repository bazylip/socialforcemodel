#!/usr/bin/env python

import socialforcemodel as sfm
import numpy as np
import matplotlib.pyplot as plt

def xPosition(world):
    for group in world.groups:
        for p in group.pedestrians:
            return p.position[0]

def peopleInRoom(world):
    counter = 0

    for group in world.groups:
        for p in group.pedestrians:
            if p.position[0] < 10:
                counter += 1
    print("People left in room: ", counter)
    return counter

def main(args):
    loader = sfm.ParameterLoader(args.file)
    world = loader.world
    world.update()


    if args.test == 1:
        world.add_measurement(xPosition)
    elif args.test == 4:
        world.add_measurement(peopleInRoom)

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

    np.savetxt("tmp/measurements" + str(args.number) + "/measurements.txt", world.measurements, fmt='%1.4f')

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
