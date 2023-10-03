from moving_average import MovingAverage

SIZE = 5

ma = MovingAverage(SIZE)

value_list = [2, 5, 4, 2, 5, 8, 9, 3]

for val in value_list:
    ma.add(val)

print(ma)