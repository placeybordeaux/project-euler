def make_list(number):
    list = []
    list.append(number)
    while number != 1:
        if number % 2  == 0: #is even
            number = number/2
        else:
            number = 3 * number + 1
        list.append(number)
    return list

def max_length_seq():
    m = 0
    longest = None
    for i in range(1,1000000):
        if m < len(make_list(i)):
            m = len(make_list(i))
            longest = i
    return longest

if __name__ == "__main__":
    print max_length_seq()
