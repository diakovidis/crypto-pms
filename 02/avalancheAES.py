#!/usr/bin/env python
import random
from Crypto.Cipher import AES


def differentBits(x, y):
    # convert Bytes to bits, Add zeros for len()=64 and split them
    x = (bin(int_from_bytes(x))[2:])
    y = (bin(int_from_bytes(y))[2:])
    x = list((64 - len(x)) * str(0) + x)
    y = list((64 - len(y)) * str(0) + y)
    counter = 0
    for i in range(0, 64):
        if (x[i] != y[i]):
            counter += 1
    return counter


def to_bytes(n, length, endianess='big'):
    h = '%x' % n
    s = ('0' * (len(h) % 2) + h).zfill(length * 2).decode('hex')
    return s if endianess == 'big' else s[::-1]


def int_from_bytes(b):
    return int(b.encode('hex'), 16)

def bitstring_to_bytes(x):
    s = ''.join(str(e) for e in x)
    return to_bytes(int(s, 2), (len(s) + 7) // 8, endianess='big')


def encryptAES_ECB(message, key):
    aes = AES.new(key, AES.MODE_ECB)
    return aes.encrypt(message)

def encryptAES_CBC(message, key):
    iv = ''.join([chr(random.randint(0, 0xFF)) for i in range(16)])
    aes = AES.new(key, AES.MODE_CBC,iv)
    return iv + aes.encrypt(message)

def reverseOneBit(binary):
    y = '{0:0128b}'.format(2 ** random.randrange(0, 61))
    return '{0:0128b}'.format(int(binary, 2) ^ int(y, 2))


if __name__ == '__main__':
    print 'Avalance Effect on AES\n'

    AESkey = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    bitLen = 128
    iterations = 40
    counterECB=0
    counterCBC=0

    for j in range(iterations):
        x = str('{0:0256b}'.format(random.getrandbits(bitLen)))
        y = reverseOneBit(x)
        xBytes = bitstring_to_bytes(x)
        yBytes = bitstring_to_bytes(y)

        Cx_ECB = encryptAES_ECB(xBytes, AESkey)
        Cy_ECB = encryptAES_ECB(yBytes, AESkey)
        counterECB += differentBits(Cx_ECB,Cy_ECB)

        Cx_CBC = encryptAES_CBC(xBytes, AESkey)
        Cy_CBC = encryptAES_CBC(yBytes, AESkey)
        counterCBC += differentBits(Cx_CBC,Cy_CBC)
    print "Average bit difference for ECB mode with message length %sbits, over %s iterations : %s" % (bitLen , iterations , (counterECB / iterations))
    print "Average bit difference for CBC mode with message length %sbits, over %s iterations : %s" % (bitLen , iterations , (counterCBC / iterations))
