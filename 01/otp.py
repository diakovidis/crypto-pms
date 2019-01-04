#!/usr/bin/env python

character_map = {'A': '00000', 'B': '00001', 'C': '00010', 'D': '00011', 'E': '00100', 'F': '00101', 'G': '00110',
                 'H': '00111', 'I': '01000', 'J': '01001', 'K': '01010', 'L': '01011', 'M': '01100', 'N': '01101',
                 'O': '01110', 'P': '01111', 'Q': '10000', 'R': '10001', 'S': '10010', 'T': '10011', 'U': '10100',
                 'V': '10101', 'W': '10110', 'X': '10111', 'Y': '11000', 'Z': '11001', '.': '11010', '!': '11011',
                 '?': '11100', '(': '11101', ')': '11110', '-': '11111'}

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


def string_to_bits(key):
    bits = []
    for c in key:
        bits.append(character_map[c.capitalize()])
    return bits


def bits_to_string(bits):
    # reverse the map
    string = []
    p = dict(zip(character_map.values(), character_map.keys()))
    for bit in bits:
        string.append(p[bit])
    return string


if __name__ == '__main__':
    print 'One Time Pad Implementation'
    print ''

    # key input
    key = raw_input('Enter an encryption key: ')
    print 'Key Characters: ', [ord(char) for char in key]
    # plaintext input
    plaintext = raw_input('Choose your plaintext: ')
    print 'Plaintext Characters: ', [ord(char) for char in plaintext]

    # if key is shorter than message, expand key
    if len(key) < len(plaintext):
        key = (key * ((len(plaintext) / len(key)) + 1))[:len(plaintext)]

    key_bits = string_to_bits(key)
    plaintext_bits = string_to_bits(plaintext)

    cipher_bits = xor(plaintext_bits, key_bits)
    ciphertext = ''.join(map(str, bits_to_string(cipher_bits)))

    print 'Ciphertext: ', ciphertext

    print 'Decrypted ciphertext: ', ''.join(map(str, bits_to_string(xor(cipher_bits, key_bits))))
