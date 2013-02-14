def euler29():
    s = set()
    for a in range(2,101):
        for b in range(2,101):
            s.add(a**b)
    return len(s)

if __name__ == "__main__":
    print euler29()
