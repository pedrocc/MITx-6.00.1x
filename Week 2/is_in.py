def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
    elif len(aStr) == 1:
        if char == aStr:
            return True
        else:
            return False

    sizeStringFinal = len(aStr)
    sizeStringBeginning = 0
    stringFinal = aStr

    if char > stringFinal[int(sizeStringFinal/2)]:
        sizeStringBeginning = int(sizeStringFinal/2)
        stringFinal = stringFinal[sizeStringBeginning:sizeStringFinal]
        sizeStringFinal = len(stringFinal)
        y = isIn(char, stringFinal)
    elif char < stringFinal[int(sizeStringFinal/2)]:
        sizeStringFinal = int(sizeStringFinal/2)
        stringFinal = stringFinal[0:sizeStringFinal]
        sizeStringFinal = len(stringFinal)
        y = isIn(char, stringFinal)
    elif char == stringFinal[int(sizeStringFinal/2)]:
        y = True
    return y


print(isIn('z', 'abcdefghijlmnopqz'))







