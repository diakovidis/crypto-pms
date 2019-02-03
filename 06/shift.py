#!/usr/bin/env python
# coding: utf-8
# -*- coding: utf-8 -*-
from collections import deque


def custom_shift(bits):
    bits_in_list = []
    for bit in bits:
        bits_in_list.append(bit)

    original = deque(bits_in_list)
    LS6 = deque(bits_in_list)
    LS10 = deque(bits_in_list)
    LS6.rotate(-6)
    LS10.rotate(-10)

    result = []
    for bit in range(0, 16):
        result.append(int(original[bit]) ^ int(LS6[bit]) ^ int(LS10[bit]))
    return result


def bitshiftEncryptASCII(word):
    for i in word:
        bits = '{:07b}'.format(ord(i)).zfill(16)
        shifted_bits = custom_shift(bits)
    print 'shifted, ', (int(''.join(map(str, shifted_bits)), 2))


def bitshiftEncryptInt(int):
    bits = "{0:b}".format(int).zfill(16)
    shifted_bits = custom_shift(bits)
    return long(''.join(map(str, shifted_bits)), 2)


if __name__ == '__main__':

    for i in range(0, 20):
        print 'encrypt(', i, ')', '=', bitshiftEncryptInt(i), bitshiftEncryptInt(i) / 1089
