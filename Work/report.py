#!/usr/bin/env python3
# report.py
#
# Exercise 7.3 
import fileparse
from stock import Stock
import tableformat
from portfolio import Portfolio

def read_portfolio(filename):
    ''' 
    Read the portfolios from the filename and return a 
    list of portfolios
    '''
    with open(filename) as lines:
        parsed = fileparse.parse_csv(lines, 
                                     select=['name','shares','price'], 
                                     types=[str,int,float])

    portfolio = [ Stock(**d)for d in parsed ]
    #portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in parsed ]

    return Portfolio(portfolio)

def read_prices(filename):
    ''' Read the prices from the filename and return a dictionary of prices '''
    with open(filename) as f:
        parsed =  dict(fileparse.parse_csv(f, 
                                           has_headers=False, 
                                           types=[str, float]))
    return parsed
 
def make_report_data(portfolio, prices):
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

def print_report(report_data, formatter):
    ''' Prints the output from the make_report function '''

    formatter.headings(['Name', 'Shares', 'Price', 'Change'])

    for name, shares, price, change in report_data:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)

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


def portfolio_report(portfolio_file, prices_file, fmt='txt'):
    ''' Produces a report using the portfolio and prices files  '''

    # Read data files
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    
    # Create report data
    report_data = make_report_data(portfolio, prices)

    # Print report data
    formatter = tableformat.create_formatter(fmt)
    print_report(report_data, formatter)

#    print_gain_loss(portfolio, prices)

def main(argv):
    if len(argv)== 3:
        portfolio_report(argv[1], argv[2])
    elif len(argv) == 4:
        portfolio_report(argv[1], argv[2], argv[3])
    else:
        raise SystemExit(f'Usage: {argv[0]} ' 'portfile pricefile')


if __name__ == '__main__':
    import sys
    main(sys.argv)
