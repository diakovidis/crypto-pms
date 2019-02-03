#!/usr/bin/env python3

from functools import reduce
from operator import xor
import re


class LFSR():
    '''An implementation of standard linear-feedback shift register.
   fill is the initial state as a list of 0s and 1s
   and taps correspond to indices in the binary number represented by the register.
   Bits on taps influence the next state. Note that taps are indices in binary notation,
   i.e. read from right to left. Example: taps = [3] on a nine-bit register
   is located on (9-1)-3 = 5th position in the array. '''

    def __init__(self, fill, taps):
        self.register = fill
        self.taps = taps

    def step(self):
        '''Advance the register by one step. All bits are shifted left by 1 and new bit
        is appended to the right tail. The new bit is a result of xor of the leaving (leftmost) bit
        and bits located at taps before the shift.'''
        new_bit = reduce(xor, [self.register[(len(self.register) - 1) - t] for t in
                               self.taps])  # binary number, read from right to left
        del self.register[0]
        self.register.append(new_bit)
        return self.register[-1]

    def __str__(self):
        return "<LFSR: {}, taps: {}>".format(''.join(map(str, self.register)), self.taps)

    character_map = {'A': '00000', 'B': '00001', 'C': '00010', 'D': '00011', 'E': '00100', 'F': '00101', 'G': '00110',
                     'H': '00111', 'I': '01000', 'J': '01001', 'K': '01010', 'L': '01011', 'M': '01100', 'N': '01101',
                     'O': '01110', 'P': '01111', 'Q': '10000', 'R': '10001', 'S': '10010', 'T': '10011', 'U': '10100',
                     'V': '10101', 'W': '10110', 'X': '10111', 'Y': '11000', 'Z': '11001', '.': '11010', '!': '11011',
                     '?': '11100', '(': '11101', ')': '11110', '-': '11111'}

    @staticmethod
    def xor(m, k):
        """Given strings m and k of characters 0 or 1,
        it returns the string representing the XOR
        between each character in the same position.
        This means that m and k should be of the same length.

        Use this function both for encrypting and decrypting!"""
        r = []
        for i, j in zip(m, k):
            r.append(str('{0:05b}'.format(int(i, 2) ^ int(j, 2))))  # xor between bits i and j
        return r

    @staticmethod
    def string_to_bits(key):
        bits = []
        for c in key:
            bits.append(LFSR.character_map[c.capitalize()])
        return bits

    @staticmethod
    def bits_to_string(bits):
        # reverse the map
        string = []
        p = dict(zip(LFSR.character_map.values(), LFSR.character_map.keys()))
        for bit in bits:
            string.append(p[bit])
        return string


def xorbits(m, k):
    """Given strings m and k of characters 0 or 1,
    it returns the string representing the XOR
    between each character in the same position.
    This means that m and k should be of the same length.

    Use this function both for encrypting and decrypting!"""
    r = []
    for i, j in zip(m, k):
        r.append(int(i, 2) ^ int(j, 2))  # xor between bits i and j
    return re.findall('.{5}', ''.join(map(str, r)))


def bits_to_string(bits):
    # reverse the map
    string = []
    p = dict(zip(LFSR.character_map.values(), LFSR.character_map.keys()))
    for bit in bits:
        string.append(p[bit])
    return string


def bruteforce(m, c):
    partial_plaintext = LFSR.string_to_bits(m)
    print m, ': ', partial_plaintext
    ciphertext = LFSR.string_to_bits(c)
    print c, ': ', ciphertext
    initial_seed = ''.join(map(str, LFSR.xor(partial_plaintext, ciphertext)))[::-1]
    print 'xor key must be', initial_seed
    # create a new register with initial state 01101000010 and tap at position 8
    register = LFSR(fill=[1, 1, 1, 0, 1, 0, 1, 0, 0, 1], taps=[9, 8, 6, 5])

    streamBits = []
    # advance the register 3 steps
    for i in range(1023):
        register.step()
        stream = ''.join(map(str, register.register))
        if (stream == initial_seed):
            print 'initial_seed: ', stream
            return register.register
        streamBits.append(re.findall('.{5}', stream)[0])
        streamBits.append(re.findall('.{5}', stream)[1])
