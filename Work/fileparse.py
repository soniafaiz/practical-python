# fileparse.py
#
# Exercise 3.5
import csv

def parse_csv(filename, select=None, type=None):
    '''
    Parse a CSV file into a list of records
    '''

    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)
        if select:
            indices = [headers.index(colname) for colname in select]
        else:
            indices = list(range(len(headers)))
        records = []
        for row in rows:
            if not row:    # Skip rows with o data
                continue
            if type:
                record = {headers[i]: func(row[i]) for func, i in zip(type,indices)}
            else:
                record = {headers[i]: row[i] for i in indices}
            records.append(record)

    return records
