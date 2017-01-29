def gcdIter(a, b):
    if a > b:
        maior = a
        menor = b
    else:
        maior = b
        menor = a
    if maior % menor == 0:
        return menor
    else:
        x = maior % menor
        maior = menor
        menor = x
        return gcdIter(maior, menor)

print(gcdIter(20,30))