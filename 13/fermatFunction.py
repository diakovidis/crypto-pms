import matplotlib.pyplot as plt

from random import randrange

import fermat


def feedback(x):
    return x * x + x - 1354363


def run():
    Xs = []
    Ys = []
    for i in range(0, sample_size):

        x = randrange(2, 10 ** 4)
        fx = abs(feedback(x))

        if fermat.is_prime(fx):
            Xs.append(x)
            Ys.append(fx)
            print  'x:', x, 'f(x):', fx, 'IS prime'

    print Xs
    print Ys
    if (plot_flag):
        plt.plot(Xs,Ys,'ro')
        plt.ylabel('some numbers')
        plt.show()


if __name__ == '__main__':
    sample_size = 200

    plot_flag = False
    run()
