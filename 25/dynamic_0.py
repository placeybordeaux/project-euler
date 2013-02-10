if __name__ == "__main__":
    last, curr = 1,1
    term = 2
    while curr < 10**999:
        term += 1
        last, curr = curr, last + curr
    print term
