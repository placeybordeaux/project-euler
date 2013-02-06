if __name__ == "__main__":
    numbers = []
    with open("triangle.txt") as f:
        for line in f.readlines():
            numbers.append(map(int,line.split()))

    for i in range(1,len(numbers)):
        for j in range(len(numbers[i])):
            if j == 0:
                numbers[i][j] += numbers[i-1][j]
            elif j == len(numbers[i]) - 1:
                numbers[i][j] += numbers[i-1][j-1]
            else:
                numbers[i][j] += max(numbers[i-1][j-1],numbers[i-1][j])

    print max(numbers[-1])
    
