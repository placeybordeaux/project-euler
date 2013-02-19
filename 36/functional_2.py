def palindromic(string):
    for a,b in zip(string,string[::-1]):
        if a != b:
            return False
    return True

def get_palindromes(upper_limit):
    for bin in yield_bin_palindromes():
        dec = int(bin,2)
        if dec > upper_limit*2:
            break
        if dec > upper_limit:
            continue
        if palindromic(str(dec)):
            yield dec

#yields binary palindromes (a recursive generator!)
def yield_bin_palindromes(first=True):
    if first:
        for i in yield_bin_palindromes(False):
            #base case hits: it will have an arbitary binary string, mirror it!
            if i and i[0] == "1":
                yield i + i[::-1] #mirror it
                yield i + "0" + i[::-1] #mirror it with 0 in the middle
                yield i + "1" + i[::-1]
    else:
        yield "" #this acts as the base case
        for i in yield_bin_palindromes(False):
            yield i + "0"
            yield i + "1"
    

if __name__ == "__main__":
    print sum(get_palindromes(1000000))
