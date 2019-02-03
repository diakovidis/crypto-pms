#!/usr/bin/env python

character_map = {'A': '00000', 'B': '00001', 'C': '00010', 'D': '00011', 'E': '00100', 'F': '00101', 'G': '00110',
                 'H': '00111', 'I': '01000', 'J': '01001', 'K': '01010', 'L': '01011', 'M': '01100', 'N': '01101',
                 'O': '01110', 'P': '01111', 'Q': '10000', 'R': '10001', 'S': '10010', 'T': '10011', 'U': '10100',
                 'V': '10101', 'W': '10110', 'X': '10111', 'Y': '11000', 'Z': '11001', '.': '11010', '!': '11011',
                 '?': '11100', '(': '11101', ')': '11110', '-': '11111'}

def string_to_bits(key):
    bits = []
    for c in key:
        bits.append(character_map[c.capitalize()])
    return bits


if __name__ == '__main__':

    print string_to_bits('i!))aiszwykqnfcyc!?secnncvch')
    print string_to_bits('qp')


