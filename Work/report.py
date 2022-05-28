#!/usr/bin/env python3
# report.py
#
# Exercise 4.4
import csv
import sys
import fileparse
import stock

def read_portfolio(filename):
    ''' Read the portfolios from the filename and return a list of portfolios'''
    with open(filename) as lines:
        parsed = fileparse.parse_csv(lines, select=['name','shares','price'], types=[str,int,float])

    portfolio = [ stock.Stock(d['name'], d['shares'], d['price']) for d in parsed ]

    return portfolio

def read_prices(filename):
    ''' Read the prices from the filename and return a dictionary of prices '''
    with open(filename) as f:
        parsed =  dict(fileparse.parse_csv(f, has_headers=False, types=[str, float]))
    return parsed
 
def make_report(portfolio, prices):
    ''' Returns a list of all the portfolio share details along with the current price '''

    price_change = []
    for stock in portfolio:
        try:
            new_price = prices[stock.name]
            change = new_price - stock.price
            price_change.append( (stock.name, stock.shares, new_price, change) )

        except KeyError:
            print('Key error: can\'t find ', stock.name)

    return price_change

def print_report(portfolio, prices):
    ''' Prints the output from the make_report function '''
    report = make_report(portfolio, prices)

    header = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % header)
    print('---------- ---------- ---------- ----------')

    for name, share, price, change in report:
        price_str = '$' + '%0.2f' % price
        print(f'{name:>10s} {share:>10d} {price_str:>10s} {change:>10.2f}')

def print_gain_loss(portfolio, prices):
    ''' Outputs the gain/loss of the portfolio '''
    portfolio_value = 0.0
    total_gain_loss = 0.0

    for stock in portfolio:
        try:
            stock_value = stock.shares * prices[stock.name]
            stock_gain_loss = stock_value - stock.shares * stock.price

            portfolio_value += stock_value
            total_gain_loss += stock_gain_loss

        except KeyError:
            print('Key error: can\'t find ', stock)

    print(f'The current portfolio value is ${portfolio_value:,.2f}')
    print(f'The total gain/loss is ${total_gain_loss:,.2f}')


def portfolio_report(portfolio_file, prices_file):
    ''' Produces a report using the portfolio and prices files  '''
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    
    print_report(portfolio, prices)
    print_gain_loss(portfolio, prices)

def main(argv):
    if len(argv) != 3:
        raise SystemExit(f'Usage: {argv[0]} ' 'portfile pricefile')
    portfolio_report(argv[1], argv[2])
    #portfolio_report('Data/portfolio.csv', 'Data/prices.csv')

if __name__ == '__main__':
    import sys
    main(sys.argv)
