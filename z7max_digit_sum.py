def digit_sum(number):
    return sum(int(digit) for digit in str(number))

def max_digit_sum(numbers):
    max_sum = 0
    max_num = None

    for num in numbers:
        sum_digits = digit_sum(num)
        if sum_digits > max_sum:
            max_sum = sum_digits
            max_num = num

    return max_num