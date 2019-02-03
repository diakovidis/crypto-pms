#!/usr/bin/env python
# coding: utf-8
# -*- coding: utf-8 -*-

import math


def fast_pow(C, d):
    text = []

    for i in C:
        result = 1
        dd = d
        while dd > 0:
            result = (result * i) % N
            dd -= 1

        text.append(result % N)

    return ''.join(map(chr, text))


def find_factors(N):
    # check for factors
    if N > 1:
        for i in range(2, N):
            if (N % i) == 0:
                return [i, N // i]
        else:
            print(N, "is a prime number")

    else:
        print(N, "is not a prime number")


def get_d(p, q, e):
    FN = (p - 1) * (q - 1)  # FΝ=11200
                            # d=e^-1modF(Ν)'''
    return (e ** (-1)) % FN #auto prepei na allaxtei, na vrethei o swstos tropos upologismou wste na vgazei swsto apotelesma 1179


if __name__ == '__main__':
    C = [3203, 909, 3143, 5255, 5343, 3203, 909, 9958, 5278, 5343, 9958, 5278, 4674, 909, 9958, 792, 909, 4132, 3143,
         9958, 3203, 5343, 792, 3143, 4443]
    N = 11413
    e = 19

    factors = find_factors(N)
    p = factors[0]
    print 'p = ', p
    q = factors[1]
    print 'q = ', q

    d = get_d(p, q, e)

    print fast_pow(C, d)
