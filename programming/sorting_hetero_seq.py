import datetime

seq = [9, 4, -3, 'Twelve', 17, datetime.date(2023, 5, 29), 'one', 0]

result = sorted(seq, key=str)

print(result)