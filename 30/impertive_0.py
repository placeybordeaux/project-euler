def sum_of_digits_to_the_fifth(number):
    sum = 0
    digit = number
    while digit != 0:
        sum += (digit%10)**5
        digit = digit/10
        if sum > number:
            return False
    return sum == number

if __name__ == "__main__":
    print reduce(lambda x,y: x + y, filter(sum_of_digits_to_the_fifth,range(1024,1000000)))

# the lower bound was found, non-rigoursly, more or less with guess work
        
