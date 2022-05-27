# fileparse.py
#
# Exercise 3.4
import csv

def parse_csv(filename, select=None):
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
            record = {headers[i]: row[i] for i in indices}
            records.append(record)

    return records
