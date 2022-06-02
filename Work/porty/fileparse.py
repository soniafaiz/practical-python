# fileparse.py
#
# Exercise 3.10
import csv
import logging
log = logging.getLogger(__name__)

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a csv file or lines into a list of records
    '''

    if not silence_errors and not has_headers and select:
        raise RuntimeError('select argument requires column headers.')

    lines = csv.reader(lines, delimiter=delimiter)

    if has_headers:
        # Read the file headers and save indices
        headers = next(lines) #next(rows)
        if select:
            indices = [headers.index(colname) for colname in select]
        else:
            indices = list(range(len(headers)))

    records = []
    for rowno, row in enumerate(lines):
        if not row:    # Skip rows with o data
            continue

        try:
            if types:
                row = [func(val) for func,val in zip(types,row)]
    
            if has_headers:
                record = {headers[i]: row[i] for i in indices}
            else:
                record = row

            records.append(record)

        except ValueError as e:
            if not silence_errors:
                log.warning(f'W:Row {rowno}: Couldn\'t convert {row}')
                log.debug(f'D:Row {rowno}: Reason: {e}')

    return records
