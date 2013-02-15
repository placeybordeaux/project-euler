def multi_pandigital(a,b,c):
    string = str(a) + str(b) + str(c)
    if len(string) != 9:
        return False
    for digit in "123456789":
        if string.count(digit) != 1:
            return False
    return True

def euler32():
    i,j = 1,2
    products = set()
    while True:
        c = i
        while c < 10000:
            c = i*j
            if multi_pandigital(i,j,c):
                products.add(c)
                
            j += 1
        i += 1
        j = i + 1
        if i > 1000:
            return sum(products)
        
print euler32()
