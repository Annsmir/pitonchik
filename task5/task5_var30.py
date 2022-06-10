import math


def main(x, z, y):
    q = 0
    n = len(x)
    for i in range(1, n + 1):
        q += (75 * x[i - 1] - 80 * z[math.ceil(i / 4) - 1] ** 2 - y[math.ceil(i / 4) - 1] ** 3) ** 5
    return 91 * q


if __name__ == "__main__":
    print('{:.2e}'.format(main([1.0, 0.6, 0.21],
                               [0.09, 0.74, 0.6],
                               [0.9, 0.94, 0.2])))
