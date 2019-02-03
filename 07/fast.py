def dec_to_bin(x):
    # decimal to binary list
    return [int(x) for x in bin(x)[2:]]

def fast(base, power, N):

    x = base
    d = 1
    # get the bits of power as a list of int
    g = dec_to_bin(power)
    #reverse list
    g.reverse()
    # for each bit in list
    for i in g:
        if i == 1:
            d = (d * x ) % N
        x = (x*x) % N
    return d

if __name__ == '__main__':

    print '2^1234567 mod 12345 is ', fast(2, 1234567, 12345)
    print '130^7654321 mod 56  is ', fast(130, 7654321, 567)
