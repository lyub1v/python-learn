
for b in range(1, 101):
    for k in range(1, 101):
        t = 100 - b - k
        if t > 0:
            total_cost = 10 * b + 5 * k + 0.5 * t
            if total_cost == 100:
                print('Быков:', b, 'Коров:', k, 'Телят:', t)