# tableformat.py
#
# Exercise 4.10

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headers.
        '''
        raise NotImplementedError()

    def row(sel, rowdata):
        '''
        Emit a single row of data.
        '''
        raise NotImplementedError()
     
class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''

    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Emit a table in HTML format
    '''

    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')

def create_formatter(fmt='txt'):
    '''
    Returns a formatter based on what is asked for
    '''
    if fmt == 'txt':
        formatter = TextTableFormatter()
    elif fmt == 'csv':
        formatter = CSVTableFormatter()
    elif fmt == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {fmt}')
    return formatter

def print_table(portfolio, headers, formatter):
    '''
    '''
    formatter.headings(headers)
    rowdata = []
    for stock in portfolio:
        formatter.row([getattr(stock,colname) for colname in headers])
