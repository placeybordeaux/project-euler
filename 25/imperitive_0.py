def fib():
    numbers = [1,1]
    term = 2
    yield (1,1)
    yield (2,1)
    while True:
        term += 1
        numbers[term%2] += numbers[term%2 - 1]
        yield (term,numbers[term%2])

for i in fib():
    if i[1] > 10**999:
        print i[0]
        break
