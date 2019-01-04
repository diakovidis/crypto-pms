#!/usr/bin/env python

import sys

def crypt(key, data):
    S = list(range(256))
    j = 0

    for i in list(range(256)):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]

    j = 0
    y = 0
    out = []

    for char in data:
        j = (j + 1) % 256
        y = (y + S[j]) % 256
        S[j], S[y] = S[y], S[j]

        if version == 2:
            out.append(unichr(ord(char) ^ S[(S[j] + S[y]) % 256]))

        if version == 3:
            out.append(chr(ord(char) ^ S[(S[j] + S[y]) % 256]))

    return ''.join(out)


if __name__ == '__main__':
    if sys.version_info.major == 2:
        version = 2

    else:
        version = 3
    print 'RC4 Implementation'
    print ''

    # key input
    key = raw_input('Enter an encryption key: ')
    print 'Key Characters: ', [ord(char) for char in key]

    # plaintext input
    plaintext = raw_input('Choose your plaintext: ')
    print 'Plaintext Characters: ', [ord(char) for char in plaintext]

    # encrypt
    encrypted = crypt(key, plaintext)
    print('UNICODE Ciphertext: ' + encrypted)
    print('ASCII[replace] Ciphertext: ' + encrypted.encode('ascii','replace'))

    # decrypt
    decrypted = crypt(key, encrypted)
    print('Decrypted Ciphertext: ' + decrypted)
