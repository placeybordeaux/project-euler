import os
__dir__ = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(__dir__,"names.txt")) as names:
    names = sorted(names.read().split(","))
    total = 0
    for i in range(len(names)):
        name = names[i].strip('"')
        total += sum([ord(char) - 64 for char in name]) * (i+1)
    print total
