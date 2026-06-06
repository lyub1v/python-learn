n = int(input())
last_digit = n % 10
is_same = True
while n != 0:
    current_digit = n % 10
    if current_digit != last_digit:
        is_same = False
        break
    n = n // 10
if is_same == True:
    print("YES")
else:
    print("NO")