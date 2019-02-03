#!/usr/bin/env python
# coding: utf-8
# -*- coding: utf-8 -*-

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


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def get_d(p, q, e):
    fn = (p - 1) * (q - 1)
    return modinv(e, fn)


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
