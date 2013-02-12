def sum_for_box(n):
    if n == 1: return n
    return (n*n)*4 - (n-1)*6
    #non reduced function is as follows
    #m + m - (n-1) + m - (n-1)*2 + m - (n-1)*3

if __name__ == "__main__":
    print sum(map(sum_for_box,range(1,1002,2)))
