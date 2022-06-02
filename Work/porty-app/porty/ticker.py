# ticker.py
#
#  Exercise 6.12
from .follow import follow
import csv

def select_columns(rows, indices):
    return ( [row[index] for index in indices] for row in rows )

def convert_types(rows, types):
    return ( [func(val) for func, val in zip(types, row)] for row in rows )

def make_dicts(rows, headers):
    return ( dict(zip(headers, row)) for row in rows )

def filter_symbols(rows, names):
    return (row for row in rows if row['name'] in names)

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
        formatter.row( str(row[key]) for key in row )
    

if __name__ == '__main__':
    lines = follow('Data/stocklog.csv')
    rows = parse_stock_data(lines)

    import report
    portfolio = report.read_portfolio('Data/portfolio.csv')

    rows = filter_symbols(rows, portfolio)
    for row in rows:
        print(row)
