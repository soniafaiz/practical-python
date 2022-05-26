# report.py
#
# Exercise 2.4, 2.6, 2.7, 2.9, 2.10, 2.11, 2.12
import csv
 
def read_portfolio(filename):
    ''' Read the portfolios from the filename and return a list of portfolios'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            holding = {header[0]:row[0], header[1]:int(row[1]), header[2]:float(row[2])}
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    ''' Read the prices from the filename and return a dictionary of prices '''
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except (ValueError, IndexError):
                print(f'Cant parse: {row} in file {filename}.')
    return prices                

def make_report(portfolio, prices):
    ''' Returns a list of all the portfolio share details along with the current price '''
    price_change = []

    for stock in portfolio:
        try:
            change = prices[stock['name']] - stock['price']
            price_change.append( (stock['name'], stock['shares'], stock['price'], change) )

        except KeyError:
            print('Key error: can\'t find ', stock)

    return price_change

def print_make_report():
    ''' Prints the output from the make_report function '''
    portfolio = read_portfolio('Data/portfolio.csv')
    prices = read_prices('Data/prices.csv')
    report = make_report(portfolio, prices)

    header = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % header)
    print('---------- ---------- ---------- ----------')

    for name, share, price, change in report:
        price_str = '$' + '%0.2f' % price
        print(f'{name:>10s} {share:>10d} {price_str:>10s} {change:>10.2f}')

def print_gain_loss():
    ''' Outputs the gain/loss of the portfolio '''
    portfolio_value = 0.0
    total_gain_loss = 0.0

    portfolio = read_portfolio('Data/portfolio.csv')
    prices = read_prices('Data/prices.csv')

    for stock in portfolio:
        try:
            stock_value = stock['shares'] * prices[stock['name']]
            stock_gain_loss = stock_value - stock['shares'] * stock['price']

            portfolio_value += stock_value
            total_gain_loss += stock_gain_loss

        except KeyError:
            print('Key error: can\'t find ', stock)

    print(f'The current portfolio value is ${portfolio_value:,.2f}')
    print(f'The total gain/loss is ${total_gain_loss:,.2f}')
