class primes:
    def __init__(self,n):
        self.primes = [2,3]
        self.generate_primes(n)

    def generate_primes(self,n):
        for i in range(max(self.primes),n + 1):
            if not any(filter(lambda x: i%x == 0, self.primes)):
                self.primes.append(i)

    def is_prime(self,n):
        if n == 1: return True
        if n > max(self.primes):
            self.generate_primes(n)
        return n in self.primes
    
def number_of_primes(a,b,p=None):
    if p == None:
        p = primes(10)
    n = 0
    while p.is_prime(n*n + a*n + b):
        n += 1
    return n

if __name__ == "__main__":
    p = primes(10)
    m = 0
    answer = None
    for a in range(-1000,1001):
        for b in range(-1000,1001):
            n = 0
            count = 0
            while p.is_prime(n*n + a*n + b):
                n += 1
                count += 1
            if m < count:
                print a*b
                m = count
