import math


def main(y):
    if y < -14:
        return (y ** 3) / 49 - 24 * ((1 - (y ** 3)) ** 4)
    elif -14 <= y < 61:
        return 18 * (((y ** 2) / 18 - 81 * (y ** 3)) ** 4) - 92 * (47 - y)
    elif y >= 61:
        return (math.cos(y) ** 6) - 30 * (y ** 2) - 93
