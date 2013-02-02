
def find_seq_len(number):
    if number == 1:
        return 1
    else:
        if number % 2 == 0: #is even
            number = number/2
        else:
            number = 3 * number + 1
        return 1 + find_seq_len(number)

def max_length_seq():
    m = 0
    longest = None
    function = find_seq_len
    for i in range(1,1000000):
        if m < function(i):
            m = function(i) 
            longest = i
    return longest

if __name__ == "__main__":
    print max_length_seq()
