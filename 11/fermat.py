import cProfile
from random import getrandbits


def isqrt_2(n):
    if n < 0:
        raise ValueError('Square root is not defined for negative numbers.')
    x = int(n)

    if x == 0:
        return 0
    a, b = divmod(x.bit_length(), 2)
    n = 2 ** (a + b)
    while True:
        y = (n + x // n) >> 1
        if y >= n:
            return n
        n = y


def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step


def is_prime(num):
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    return all(num % i for i in mrange(3, rounds, 2))


def generate_prime_candidate(length):
    """ Generate an odd integer randomly
        Args: length -- int -- the length of the number to generate, in bits return a integer
    """
    # generate random bits
    p = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p


def generate_prime_number(length):
    """ Generate a prime
        Args: length -- int -- length of the prime to generate, in bits return a prime
    """
    p = 4
    # keep generating while the primality test fail
    while not is_prime(p):
        p = generate_prime_candidate(length)
    return p


if __name__ == '__main__':
    rounds = 10 ** 7  # 10 000 000 rounds
    cProfile.run('print generate_prime_number(2048)')
