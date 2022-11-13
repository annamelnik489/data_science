#!/usr/bin/env python

import re
import sys
from pathlib import Path

DATA_DIR_FORMAT='{}/data_1'
OUTPUT_FILENAME_FORMAT = '{}/{}'

def clean_first_row(line):
    line = re.sub('<br>', ' ', line)
    return re.sub('  ', ' ', line, )

def clean_second_row(line):
    line = re.sub('<[^>]+>', '', line)
    return re.sub(' ', '', line)

def clean_third_row(line):
    return re.sub('<[^>]+>', '', line)

def clean_data(input_dir, output_dir):
    data_files = Path(input_dir).glob('*.csv')
    for filename in data_files:
        output_file = OUTPUT_FILENAME_FORMAT.format(output_dir, filename.name)
        with open(filename, 'r') as inp, open(output_file, 'w') as out:
            for i, line in enumerate(inp.readlines()):
                if i == 0:
                    line = clean_first_row(line)
                elif i == 1:
                    line = clean_second_row(line)
                elif i == 2:
                    line = clean_third_row(line)
                if '</pre></tt>' not in line:
                    out.write(line)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        input_dir = Path(sys.argv[1])
        if input_dir.exists():
            output_dir = Path(DATA_DIR_FORMAT.format(Path.cwd()))
            if not output_dir.exists():
                output_dir.mkdir()
            clean_data(input_dir, output_dir)
        else:
            print('Data dir {} does not exists'.format(input_dir))
    else:
        print('Usage: {} <directory with data files>'.format(sys.argv[0]))
