# pcost.py
#
# Exercise 3.14
import csv
import sys
import report

def portfolio_cost(filename):
    ''' Returns the purchase cost of the portfolio '''

    portfolio = report.read_portfolio(filename)
    total_cost = sum([row['shares']*row['price'] for row in portfolio])
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
'''
cost = portfolioCost(filename)
print(f'Total cost: {cost:10.2f}')
'''
