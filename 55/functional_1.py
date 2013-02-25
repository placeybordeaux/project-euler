def palindrome(n):
    n = str(n)
    return n == n[::-1]

def lychrel(n):
    for i in range(50):
        n += int(str(n)[::-1])
        if palindrome(n):
            return False
    return True
    
print len(filter(lychrel,range(10000)))
