def memoize(f):
    cache = {}
    def g(x,y):
        if (x,y) not in cache:
            cache[(x,y)] = f(x,y)
        return cache[(x,y)]
    return g

@memoize
def f(downs,lefts):
    if downs > 0 and lefts > 0:
        return f(downs - 1,lefts) + f(downs, lefts - 1)
    else:
        return 1

if __name__ == "__main__":
    print f(20,20)
