n = int(input())
last= n % 10
minn = last
maxn = last
while n !=0:
    last = n %10
    if minn > last:
        minn = last
    if maxn < last:
        maxn = last
    n = n // 10
print('Максимальная цифра равна', maxn)
print('Минимальная цифра равна', minn)

