#!/usr/bin/env python3
"""
The csv file must contain a "title" column and any main content should be in a "body" column.

https://discourse.gohugo.io/t/solved-using-csv-file-to-create-individual-posts-on-build/19059/11
"""

import csv
import re
import unicodedata

from pathlib import Path

# Set the path to the source CSV file.
source = Path('/Users/frjo/Desktop/test.csv')


def slugify(value):
    value = str(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    return re.sub(r'[-\s]+', '-', value)


def write(path, row):
    file = open(path, 'w')
    print('---', file=file)
    for key, value in row.items():
        if key != 'body':
            print(f'{key}: "{value}"', file=file)
    print('\n---\n', file=file)
    if 'body' in row:
        print(row['body'], file=file)


def main():
    csv_file = open(source, newline='')
    csv_content = csv.DictReader(csv_file)
    for row in csv_content:
        filename = slugify(row['title'])
        path = Path(f'{filename}.md')
        if not path.is_file():
            write(path, row)


if __name__ == '__main__':
    main()