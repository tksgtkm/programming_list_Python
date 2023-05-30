from pprint import pprint

prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

p1 = {key:value for key, value in prices.items() if value > 200}

print("All prices over 200")
pprint(p1)

tech_names = {'APPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key:value for key, value in prices.items() if key in tech_names}

print("All techs")
pprint(p2)