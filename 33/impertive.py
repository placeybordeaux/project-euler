import operator
from fractions import Fraction

def curious(a,b):
    #try statment to catch the possible divisions by zero. Could be faster to check for them by hand, but I think this is cleaner
    try:
        c = float(a)/b
        #case for xa/xb == a/b
        if a/10 == b/10:
            if float(a%10)/(b%10) == c:
                return 1
        #case for xa/bx == a/b
        if a/10 == b%10:
            if float(a%10)/(b/10) == c:
                return 1
        #case for ax/xb == a/b
        if a%10 == b/10:
            if float(a/10)/(b%10) == c:
                return 1
        #case for ax/bx == a/b
        if a%10 == b%10:
            if float(a/10)/(b/10) == c:
                return 1
    except:
        pass
    return 0

if __name__ == "__main__":
    fraction = Fraction(1,1)
    for a in range(10,99):
        for b in range(a + 1,99):
            if curious(a,b):
                if a%10 and b%10:
                     fraction *= Fraction(a,b)

    print fraction

