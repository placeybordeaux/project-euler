import operator

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

def reduce_fract(a,b):
    for i in range(2,a + 1):
        if a%i == 0 and b%i == 0:
            a /= i
            b /= i
            return reduce_fract(a,b)
    return (a,b)

if __name__ == "__main__":
    list = []            
    for a in range(10,99):
        for b in range(a + 1,99):
            if curious(a,b):
                if a%10 and b%10:
                     list.append(reduce_fract(a,b))

    numerator = reduce(operator.mul,[x[0] for x in list])
    denominator = reduce(operator.mul,[x[1] for x in list]) 
    print reduce_fract(numerator,denominator)

