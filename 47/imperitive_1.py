#18391.698 seconds :(
from math import sqrt

def divisors(number):
    divisors = set()
    for i in range(2,number):
        while number%i == 0:
            divisors.add(i)
            number /= i
        if len(divisors) > 4:
            return []
        if i**2 > number:
            return divisors
    return divisors

i = 1
counter = 0
while True:
    if len(divisors(i)) == 4:
        counter += 1
    else:
        counter = 0
    if counter == 4:
        print i - 3
        break
    i += 1
