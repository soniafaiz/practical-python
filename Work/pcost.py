# pcost.py
#
# Exercise 1.33
import csv
import sys

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

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolioCost(filename)
print(f'Total cost: {cost:10.2f}')
