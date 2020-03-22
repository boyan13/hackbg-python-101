#Sum of all digits of a number

def sum_of_digits(n):
    sum = 0

    if (n < 0):
        n *= -1

    while (n > 0):
        sum += n%10
        n //= 10

    return sum


print( sum_of_digits(1325132435356) ) #43
print( sum_of_digits(123)           ) #6
print( sum_of_digits(6)             ) #6
print( sum_of_digits(-10)           ) #1
