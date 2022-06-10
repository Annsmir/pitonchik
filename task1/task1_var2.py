import math


def main(x, y):
    return (math.floor(0.02 + (y ** 2) + (x ** 3)) ** 2) \
           / ((71 * y + 59 + 39 * (y ** 3)) ** 2
              + ((math.cos(x) ** 4) / 50)) + 19 * \
           (math.acos((x ** 3) - 48 * (y ** 2) - 1)) ** 3 \
           - math.acos((x ** 2) + 53 * (y ** 3)) ** 5
