n = int(input())
last_digit = n % 10
digit_sum = 0
digit_count = 0
digit_mult = 1
first_digit = 0
if n == 0:
    digit_sum = 0
    digit_count = 1
    digit_mult = 0
    first_digit = 0
else:
    while n != 0:
        current_digit = n % 10
        digit_sum += current_digit
        digit_count += 1
        digit_mult *= current_digit
        first_digit = current_digit
        n = n // 10
mean_output = digit_sum / digit_count
first_plus_last = first_digit + last_digit
print(digit_sum)
print(digit_count)
print(digit_mult)
print(mean_output)
print(first_digit)
print(first_plus_last)