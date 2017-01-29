def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a > b:
        bigger = a
        smaller = b
    else:
        bigger = b
        smaller = a
    if bigger % smaller == 0:
        return smaller

    contador = smaller - 1
    while contador >= 0:
        if bigger % contador == 0:
            if smaller % contador == 0:
                return contador
        contador -= 1

print(gcdIter(100,30))

