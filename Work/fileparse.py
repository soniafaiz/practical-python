# fileparse.py
#
# Exercise 3.7
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
    '''
    Parse a CSV file into a list of records
    '''

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers
        if has_headers:
            headers = next(rows)
            if select:
                indices = [headers.index(colname) for colname in select]
            else:
                indices = list(range(len(headers)))

        records = []
        for row in rows:
            if not row:    # Skip rows with o data
                continue
            if has_headers:
                if types:
                    record = {headers[i]: func(row[i]) for func, i in zip(types,indices)}
                else:
                    record = {headers[i]: row[i] for i in indices}
            else:
                if types:
                    record = tuple([func(val) for func,val in zip(types,row)])

                else:
                    record = row

            records.append(record)

    return records
