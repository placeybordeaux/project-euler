from itertools import count

def euler52():
    for i in count(1):
        numbers = set(str(i))
        for m in range(2,7):
            if numbers == set(str(i*m)):
                if m == 6:
                    return i
            else:
                break #breaks out of the loop checking all of the multiplicants

print euler52()
