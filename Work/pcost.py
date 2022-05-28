# pcost.py
#
# Exercise 3.15
import csv
import report

def portfolio_cost(filename):
    ''' Returns the purchase cost of the portfolio '''

    portfolio = report.read_portfolio(filename)
    total_cost = sum([row['shares']*row['price'] for row in portfolio])
    return total_cost

def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: {argv[0]} ' 'portfile')
    filename = argv[1]
    cost = portfolio_cost(filename)
    print(f'Total cost: {cost:10.2f}')

if __name__ == '__main__':
    import sys
    main(sys.argv)
