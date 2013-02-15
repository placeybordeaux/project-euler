from math import log10 as log

def canidates():
    for i in range(1,10000):
        for j in range(i,10000):
            ij = i*j
            if int(log(i)) + int(log(j)) + int(log(ij)) + 3 == 9:
                yield (i,j,ij)
            elif int(log(i)) + int(log(j)) + int(log(ij)) + 3 > 9:
                break

def is_pandigital(canidate):
    canidate = ''.join(map(str,canidate))
    for digit in "123456789":
        if canidate.count(digit) != 1:
            return False
    return True

print sum(set(map(lambda x: x[2],filter(is_pandigital,canidates()))))
