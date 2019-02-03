#!/usr/bin/env python
# coding: utf-8
# -*- coding: utf-8 -*-

import math
from decimal import *
import math

getcontext().prec = 40


def euclid_algo(b, a):
    r0 = a
    r1 = b
    r2 = 1
    ques = []
    while (r2 > 0):
        q = r0 / r1
        ques.append(q)
        r2 = r0 - q * r1
        r0 = r1
        r1 = r2
    return ques


def get_p_q(n, b):
    q = euclid_algo(n, b)
    c = [1, q[0]]
    d = [0, 1]
    for j in range(1, len(q)):
        if c[j] != 0:
            n1 = (d[j] * b - 1) / c[j]
            if n1 % 1 == 0:
                prod = n - n1 + 1
                descrim = Decimal(prod * prod - 4 * n)
                if descrim >= 0:
                    sqrtdesc = descrim.sqrt()
                    if sqrtdesc._isinteger():
                        p1 = (prod + sqrtdesc)
                        p2 = (prod - sqrtdesc)
                        if p1 % 2 == 0 and p2 % 2 == 0:
                            p1 = p1 / 2
                            p2 = p2 / 2
                        if p1 > 0 and p2 > 0:
                            if p1 < n and p2 < n:
                                return p1, p2
        c.append(q[j] * c[j] + c[j - 1])
        d.append(q[j] * d[j] + d[j - 1])
    print "Wiener's attack failed"
    return 0


def dec_to_bin(x):
    # decimal to binary list
    return [int(x) for x in bin(x)[2:]]


def fast(base, power, N):
    x = base
    d = 1
    # get the bits of power as a list of int
    g = dec_to_bin(int(power))
    # reverse list
    g.reverse()
    # for each bit in list
    for i in g:
        if i == 1:
            d = (d * x) % N
        x = (x * x) % N
    return d


def fast_pow(C, d):
    text = []
    for i in C:
        text.append(fast(i, d, N))

    return ''.join(map(chr, text))


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
    C = [47406263192693509, 51065178201172223, 30260565235128704, 82385963334404268,
         8169156663927929, 47406263192693509, 178275977336696442, 134434295894803806,
         112111571835512307, 119391151761050882, 30260565235128704, 82385963334404268,
         134434295894803806, 47406263192693509, 45815320972560202, 174632229312041248,
         30260565235128704, 47406263192693509, 119391151761050882, 57208077766585306,
         134434295894803806, 47406263192693509, 119391151761050882, 47406263192693509,
         112111571835512307, 52882851026072507, 119391151761050882, 57208077766585306,
         119391151761050882, 112111571835512307, 8169156663927929, 134434295894803806,
         57208077766585306, 47406263192693509, 185582105275050932, 174632229312041248,
         134434295894803806, 82385963334404268, 172565386393443624, 106356501893546401,
         8169156663927929, 47406263192693509, 10361059720610816, 134434295894803806,
         119391151761050882, 172565386393443624, 47406263192693509, 8169156663927929,
         52882851026072507, 119391151761050882, 8169156663927929, 47406263192693509,
         45815320972560202, 174632229312041248, 30260565235128704, 47406263192693509,
         52882851026072507, 119391151761050882, 111523408212481879, 134434295894803806,
         47406263192693509, 112111571835512307, 52882851026072507, 119391151761050882,
         57208077766585306, 119391151761050882, 112111571835512307, 8169156663927929,
         134434295894803806, 57208077766585306]

    N = 194749497518847283
    e = 50736902528669041

    d = get_p_q(N, e)  # Wiener attack on N, e
    p = d[0]
    q = d[1]
    print 'p = ', p
    print 'q = ', q

    d = get_d(p, q, e)

    print fast_pow(C, d)
