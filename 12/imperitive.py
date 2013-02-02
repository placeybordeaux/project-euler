import math 

def triangles():
    i = 1
    tri = 0
    while 1:
        tri += i
        i += 1
        yield tri

def divisors(number):
    count = 1
    for i in range(1,int(math.sqrt(number) + 1)):
        if number%i == 0:
            count += 2
    return count

if __name__ == "__main__":
    for i in triangles():
        if divisors(i) > 500:
            print "found it:",i
            break
