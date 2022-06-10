import math


def main(x):
    if x < 20:
        return 52 * (37 * x ** 2 - 85 * x) + 10 * x ** 2
    elif 20 <= x < 56:
        return x ** 6
    elif x >= 56:
        return 86 * math.ceil(x) ** 4 - x - 69 * (0.01 - 16 * x ** 3 - 69 * x) ** 7


if __name__ == "__main__":
    print('{:.2e}'.format(main(141)))