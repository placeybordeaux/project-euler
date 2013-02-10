class fib:
    counter = 2
    numbers = []
    def __init__(self,n = 1):
        self.numbers = [1,1]
        counter = 2

    def first_term_over(self,n):
        temp = (self.counter)%2
        while self.numbers[temp] < n:
            self.counter += 1
            temp = (self.counter)%2
            self.numbers[temp] = self.numbers[temp] + self.numbers[temp - 1]
        return self.counter

if __name__ == "__main__":
    f = fib()
    print f.first_term_over(10**999)
