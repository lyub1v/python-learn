n = int(input())
last_digit = n % 10
count_three = 0
count_last_digit = 0
count_even = 0
sum_greater_five = 0
mult_greater_seven = 1
count_zero_and_five = 0
while n > 0:
    digit = n % 10
    if digit == 3:
        count_three += 1
    if digit == last_digit:
        count_last_digit += 1
    if digit % 2 == 0:
        count_even += 1
    if digit > 5:
        sum_greater_five += digit
    if digit > 7:
        mult_greater_seven *= digit
    if digit == 0 or digit == 5:
        count_zero_and_five += 1
    n //= 10
print(count_three)
print(count_last_digit)
print(count_even)
print(sum_greater_five)
print(mult_greater_seven)
print(count_zero_and_five)