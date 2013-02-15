def get_digits(number):
    while number != 0:
        yield number%10
        number /= 10

def is_sum_of_digits_to_fifth(number):
    return number == sum(map(lambda x: x**5,get_digits(number)))

if __name__ == "__main__":
    print sum(filter(is_sum_of_digits_to_fifth,range(1024,354294)))

# the lower bound was found, non-rigoursly, more or less with guess work
