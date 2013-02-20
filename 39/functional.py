from math import sqrt
def solutions(p):
    count = 0
    for c in range(1,p/2):
        for a in range(1,min(c,(p-c)/2)):
            if sqrt(c**2 - a**2) == p - (c + a):
                count += 1
                break #there can only be one solution for each c, otherwise a will assume b's current value

    return count

print solutions(120)
print max(range(1,1001), key=lambda x: solutions(x))
