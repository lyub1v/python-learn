s = input()
count = 0
count2 = 0

for char in s:
    if char == '*':
        count += 1
    elif char == '+':
        count2 += 1

print('Символ + встречается', count2, 'раз')
print('Символ * встречается', count, 'раз')


