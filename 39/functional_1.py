#I would recommend using pypy for this, many orders of magnitude faster than cPython

from math import sqrt

def solutions(p):
    count = 0
    #gets all of the possible perimeter values, should top out at p * 3/2
    possibles = [sqrt(a**2 - c**2) + a + c for a in range(1,p/2) for c in range(1,a)]
    return sum(filter(lambda x: x == p,possibles))

#sorts the perimeter values by the number of solutions they have
print max(range(1,1001), key=lambda x: solutions(x))
