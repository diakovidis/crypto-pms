import cProfile
from random import randrange

import fermat


def feedback(x):
    return x * x + x - 1354363


def run():
    Xs = []
    Ys = []
    for i in range(0, 200):

        x = randrange(2, 10 ** 4)
        fx = abs(feedback(x))

        if fermat.is_prime(fx):
            Xs.append(x)
            Ys.append(fx)
            print  x, fermat.is_prime(x), fx, 'IS prime'
        # else:
        #     print i, x, fx
    print Xs
    print Ys


if __name__ == '__main__':
    rounds = 10 ** 7
    run()
