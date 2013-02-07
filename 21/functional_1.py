import math

def memoize(f):
    cache = {}
    def g(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return g

@memoize
def sum_o_divisors(number):
    sum = 1
    for i in range(2,int(math.sqrt(number))):
        if number%i == 0:
            sum += i
            sum += number/i
    return sum

#if sum_o_divisors(n) == m and sum_o_divisors(m) == n, then n and m are 'amicable'

def amicable(n):
   if sum_o_divisors(n) == n: return False 
   if sum_o_divisors(sum_o_divisors(n)) != n: return False
   return True 
   

print sum(filter(amicable, range(10000)))
