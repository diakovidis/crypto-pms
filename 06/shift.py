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


def decode(string):
    print 'text: ', string
    bit_list_string = string_to_bits(string)
    print 'as binary: ', bit_list_string

    bit_list_int = []
    bit_list_decoded = []

    for bit_str in bit_list_string:
        bit_as_int = []
        for c in bit_str:
            bit_as_int.append(int(c))
        bit_list_int.append(bit_as_int)

    for bit_sequence in bit_list_int:
        for m in bit_sequence:
            tmp1 = m << 6
            tmp2 = m << 10
            bit_list_decoded.append(m ^ tmp1 ^ tmp2)

    return bit_list_decoded


def bitshiftEncrypt(word):
    newWord = ""
    for i in word:
        shift = '{:07b}'.format(ord(i) + 1).zfill(16)
        newShift = shift[1:]
        newShift += shift[0]
        newWord += chr(int(newShift, 2))
    print(newWord)


def bytes2int(str):
    res = ord(str[0])
    for ch in str[1:]:
        res <<= 8
        res |= ord(ch)
    return res


def int2bytes(n):
    res = []
    while n:
        ch = n & 0b11111111
        res.append(chr(ch))
        n >>= 8
    return ''.join(reversed(res))


if __name__ == '__main__':
    # print 'decode', decode('b')
    bytes = 'abcdefghijklmnopqrstuv'

    print 'abcdefghijklmnopqrstuv', (bytes2int(bytes))
