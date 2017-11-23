# See: https://projecteuler.net/problem=360

import logging, sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


def is_on_sphere(x, y, z, r):
    """
    Is the point given by (x, y, z) on the surface of the sphere of radius r?
    """
    return x**2 + y**2 + z**2 == r**2


def integer_points_on_sphere(r):
    for x in range(-r, r+1):
        for y in range(-r, r+1):
            for z in range(-r, r+1):
                if is_on_sphere(x, y, z, r):
                    yield (x, y, z)


def manhatten_distance_from_orgin(x, y, z):
    return abs(x) + abs(y) + abs(z)


def main(r):
    sum = 0
    for x,y,z in integer_points_on_sphere(r):
        logging.debug("point on sphere: ({},{},{})".format(x,y,z))
        sum += manhatten_distance_from_orgin(x, y, z)
    return sum


if __name__ == "__main__":
    # The radius of the sphere
    r = 45

    print("S({}) {}".format(r, main(r)))
