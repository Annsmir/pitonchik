import math


def main(m, b, a, x):
    s1 = 0
    for i in range(1, a + 1):
        s2 = 1
        for c in range(1, b + 1):
            s3 = 0
            for k in range(1, m + 1):
                s3 += (12 * x ** 2 + k) ** 3 + \
                      (99 * c) ** 7 + 40 * math.sin(i) ** 4
            s2 *= s3
        s1 += s2
    return s1
