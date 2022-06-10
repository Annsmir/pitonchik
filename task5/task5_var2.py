import math


def main(x, y):
    q = 0
    n = len(x)
    for i in range(1, n + 1):
        q += ((x[n - math.ceil(i / 4)] - y[n - i] ** 3 - 1) ** 6) / 6
    return 54 * q


if __name__ == "__main__":
    print('{:.2e}'.format(main([0.51, -0.65, -0.53],
                               [-0.73, -0.52, 0.01])))
