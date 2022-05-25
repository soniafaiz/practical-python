# pcost.py
#
# Exercise 1.27
totalCost = 0.0
with open('Data/portfolio.csv', 'rt') as file:
    next(file)
    for line in file:
        row = line.split(',')
        totalCost += float(row[1]) * float(row[2])

print(f'Total cost: {totalCost:10.2f}')
