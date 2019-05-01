#!/usr/bin/env python

import socialforcemodel as sfm
import numpy as np
import matplotlib.pyplot as plt

def average_speed(world):
    velocities = []
    for group in world.groups:
        for p in group.pedestrians:
            velocities.append(p.speed)
    return np.mean(velocities)

def avg_num_neighbours(world):
    counts = []
    for group in world.groups:
        for p in group.pedestrians:
            counts.append(p.get_measurement('neighbourhood', 'num_neighbours'))
    return np.mean(counts)

def main(args):
    loader = sfm.ParameterLoader(args.file)
    world = loader.world
    world.update()

    world.add_measurement(average_speed)
    world.add_measurement(avg_num_neighbours)
    figure = world.plot()
    figure.savefig("img/0.png",
                   bbox_inches = 'tight',
                   pad_inches = 0.1)
    figure.clear()
    plt.close(figure)

    for step in range(args.steps):
        print "Step {}".format(step + 1)
        if not world.step():
            break
        world.update()
        if step % 5 == 4:
            figure = world.plot()
            figure.savefig("img/" + str((step + 1)/5) + ".png",
                           bbox_inches = 'tight',
                           pad_inches = 0.1)
            figure.clear()
            plt.close(figure)

    np.savetxt("measurements.txt", world.measurements)

if __name__ == '__main__':
    import argparse
    import sys
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='YAML-file')
    parser.add_argument('-s', '--steps', help='Number of steps', type=int, default=500)
    args = parser.parse_args(sys.argv[1:])
    main(args)