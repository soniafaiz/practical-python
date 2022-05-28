# fileparse.py
#
# Exercise 3.10
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''

    if not silence_errors and not has_headers and select:
        raise RuntimeError('select argument requires column headers.')

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        if has_headers:
            # Read the file headers and save indices
            headers = next(rows)
            if select:
                indices = [headers.index(colname) for colname in select]
            else:
                indices = list(range(len(headers)))

        records = []
        for rowno, row in enumerate(rows):
            if not row:    # Skip rows with o data
                continue

            try:
                if types:
                    row = [func(val) for func,val in zip(types,row)]
    
                if has_headers:
#                    if types:
#                        record = {headers[i]: func(row[i]) for func, i in zip(types,indices)}
#                    else:
                    record = {headers[i]: row[i] for i in indices}
                else:
#                    if types:
#                        record = tuple([func(val) for func,val in zip(types,row)])
#                    else:
                    record = row

                records.append(record)

            except ValueError as e:
                if not silence_errors:
                    print(f'Row {rowno}: Couldn\'t convert {row}')
                    print(f'Row {rowno}: Reason: {e}')

    return records
