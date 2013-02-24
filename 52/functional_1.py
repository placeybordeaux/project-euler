from itertools import count

def same_digits(a,b):
    return set(str(a)) == set(str(b))

def euler52():
    for i in count(1):
        if all(map(lambda x: same_digits(i,i*x),range(2,7))):
            return i

print euler52()
