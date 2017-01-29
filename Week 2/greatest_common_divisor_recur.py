def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a > b:
        maior = a
        menor = b
    else:
        maior = b
        menor = a
    if menor == 0:
        return a
    if maior % menor == 0:
        return menor
    else:
        x = maior % menor
        maior = menor
        menor = x
        return gcdRecur(maior, menor)

print(gcdRecur(100,30))
