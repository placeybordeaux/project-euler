def get_matrix(file):
    with open(file) as f:
        temp = f.readlines() #array of lines
    temp = map(lambda x: x.split(), temp) #array of array of numbers as strings
    return map(lambda x: [int(y) for y in x], temp) #array of array of numbers as ints

def get_values(array,x,y):
    values = []
    sums = []
    if x+3 < len(array): values.append(((x,y),(x+1,y),(x+2,y),(x+3,y)))
    if x > 3 and y+3 < len(array): values.append(((x,y),(x-1,y+1),(x-2,y+2),(x-3,y+3)))
    if y+3 < len(array): values.append(((x,y),(x,y+1),(x,y+2),(x,y+3)))
    if x > 3 and y > 3: values.append(((x,y),(x-1,y-1),(x-2,y-2),(x-3,y-3)))
    for value in values:
        num = 1
        for v in value:
            num *= array[v[0]][v[1]]
        sums.append(num)
    return sums
        

def get_max(array):
    m = 0
    for i in range(len(array)):
        for j in range(len(array)):
            values = get_values(array,i,j)
            if values != None: 
                values.append(m)
                m = max(v for v in values)
    return m
            

if __name__ == "__main__":
    print get_max(get_matrix("11.txt"))
