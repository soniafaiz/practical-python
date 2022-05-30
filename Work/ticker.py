# ticker.py
#
#  Exercise 6.12
from follow import follow
import csv

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0,1,4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def ticker(portfile, logfile, fmt):
    lines = follow(logfile)
    rows = parse_stock_data(lines)
    
    import report
    portfolio = report.read_portfolio(portfile)
    rows = filter_symbols(rows, portfolio)

    from tableformat import create_formatter
    formatter = create_formatter(fmt)

    formatter.headings(['Name','Price','Change'])
    for row in rows:
        formatter.row([str(row[key]) for key in row])
    

if __name__ == '__main__':
    lines = follow('Data/stocklog.csv')
    rows = parse_stock_data(lines)

    import report
    portfolio = report.read_portfolio('Data/portfolio.csv')

    rows = filter_symbols(rows, portfolio)
    for row in rows:
        print(row)
