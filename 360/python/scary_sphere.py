#! /usr/bin/env python3

from math import sqrt

# See: https://projecteuler.net/problem=360

# The radius of the sphere
r = 45
# r = 10**10

def is_on_sphere(x, y, z, r):
    """
    Is the point given by (x, y, z) on the surface of the sphere of radius r?
    """
    return x**2 + y**2 + z**2 == r**2

def integer_points_on_sphere(r):
    for x in range(-r, r+1):
        for y in range(-r, r+1):
            for z in range(-r, r+1):
                if (is_on_sphere(x, y, z, r)):
                    yield (x, y, z)


def manhatten_distance_from_orgin(x, y, z):
    return abs(x) + abs(y) + abs(z)

def main():
    sum = 0
    for x,y,z in integer_points_on_sphere(r):
        sum += manhatten_distance_from_orgin(x, y, z)
    print("S({}) {}".format(r, sum))


if __name__ == "__main__":
    main()
