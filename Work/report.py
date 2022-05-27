# report.py
#
# Exercise 2.16
import csv
import sys
 
def read_portfolio(filename):
    ''' Read the portfolios from the filename and return a list of portfolios'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(header, row))
            try:
                holding = {'name':record['name'], 'shares':int(record['shares']), 'price':float(record['price'])}
                portfolio.append(holding)
            except ValueError:
                print(f'Row {rowno}: Cant parse: {row} in file {filename}.')

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
            stock_value = stock['shares'] * prices[stock['name']]
            stock_gain_loss = stock_value - stock['shares'] * stock['price']

            portfolio_value += stock_value
            total_gain_loss += stock_gain_loss

        except KeyError:
            print('Key error: can\'t find ', stock)

    print(f'The current portfolio value is ${portfolio_value:,.2f}')
    print(f'The total gain/loss is ${total_gain_loss:,.2f}')


def portfolio_report(portfolio_file, prices_file):
    '''  ...  '''
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    
    print_report(portfolio, prices)
    print_gain_loss(portfolio, prices)

# Check for filename argument
if len(sys.argv) == 3:
    portfolio_file = sys.argv[1]
    prices_file = sys.argv[2]
    portfolio_report(portfolio_file, prices_file)
