# pcost.py
#
# Exercise 1.27

def portfolioCost(filename):
    totalCost = 0.0
    with open(filename, 'rt') as file:
        next(file)
        for line in file:
            row = line.split(',')
            totalCost += float(row[1]) * float(row[2])
    return totalCost

cost = portfolioCost('Data/portfolio.csv')
print(f'Total cost: {cost:10.2f}')
