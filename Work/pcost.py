# pcost.py
#
# Exercise 1.32
import csv

def portfolioCost(filename):
    totalCost = 0.0
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        next(rows)
        for row in rows:
            try:
                totalCost += float(row[1]) * float(row[2])
            except ValueError:
                print('Could not parse', row)
    return totalCost

cost = portfolioCost('Data/portfolio.csv')
print(f'Total cost: {cost:10.2f}')
