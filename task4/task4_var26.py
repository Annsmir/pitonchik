import math


def main(n):
    if n == 0:
        return 0.70
    elif n == 1:
        return -0.59
    elif n >= 2:
        return 1 - 88 * math.ceil(27 * main(n - 2)) - 38 * pow(math.atan(18 + main(n - 1) + 96 * main(n - 1) * main(n - 1)), 2)


print(main(1))
