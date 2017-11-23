#!/usr/bin/env python3
# See: https://projecteuler.net/problem=360

import argparse
import logging, sys
import re

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def is_on_sphere(x, y, z, r):
    """
    Is the point given by (x, y, z) on the surface of the sphere of radius r?
    """
    return x**2 + y**2 + z**2 == r**2


def integer_points_on_sphere(r):
    return ((x,y,z)
            for x in range(-r, r+1)
            for y in range(-r, r+1)
            for z in range(-r, r+1)
            if is_on_sphere(x, y, z, r))


def manhatten_distance_from_orgin(x, y, z):
    return abs(x) + abs(y) + abs(z)


def main(r):
    s = 0
    for x,y,z in integer_points_on_sphere(r):
        logging.debug("point on sphere: ({},{},{})".format(x,y,z))
        s += manhatten_distance_from_orgin(x, y, z)
    return s


def parse_args_for_radius():
    """
    Other than the obvious argument parsing, we'll also evaluate the argument
    as an expression, to allow for simple arithmetic like `10**10` or `5+1`.

    To sanitize this input against method calls, we'll remove any decimal points
    that aren't followed by a numeral.
    see: https://stackoverflow.com/a/25437733/82257
    """
    parser = argparse.ArgumentParser(description='Project Euler #360.')
    parser.add_argument('radius', help='The radius of the sphere in the problem')
    args = parser.parse_args()

    return eval(re.sub(r"\.(?![0-9])", "", args.radius), {'__builtins__': None})


if __name__ == "__main__":
    r = parse_args_for_radius()
    answer = main(r)

    print("S({}) {}".format(r, answer))
