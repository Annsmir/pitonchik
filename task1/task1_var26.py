from math import sqrt


def main(y, x, z):
    return sqrt(pow(y, 2) + 81 * pow(z, 3) + z + 28 * pow(pow(x, 3) - pow(y, 2), 7)) - sqrt(
        42 * pow(z, 3) + pow(pow(y, 2) - 36 * pow(x, 3) - x, 6))


print(main(0.13, -0.18, 0.44))
