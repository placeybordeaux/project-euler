def product_pandigital(n):
    string = ""
    for i in range(1,10):
        string += str(n*i)
        if len(string) == 9:
            if ''.join(sorted(string)) == "123456789":
                return int(string)
        elif len(string) > 9:
            return 0

print max(map(product_pandigital,range(9,90000)))
