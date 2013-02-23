def make_str():
    n = 0
    string = ""
    while len(string) < 1000001:
        string += str(n)
        n += 1
    return string

string = make_str()
print int(string[1]) * int(string[10]) * int(string[100]) * int(string[1000]) * int(string[10000]) * int(string[100000]) * int(string[1000000])
