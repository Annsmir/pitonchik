import math


def main(n):
    if n == 0:
        return -0.86
    if n >= 1:
        return math.exp(main(n - 1)) ** 2 / 18 + main(n - 1) ** 3
