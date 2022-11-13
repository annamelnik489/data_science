#!/usr/bin/env python

import re
import sys
from pathlib import Path


DATA_DIR_FORMAT='{}/data_2'
OUTPUT_FILENAME_FORMAT = '{}/{}'
REGION_RE = re.compile('^.*Province= *(\d+):')
REPLACE_REGION_RE = re.compile(r'(?P<reg>Province= *)\d+:')

ukr_idx = {
    1: "Вінницька",
    2: "Волинська",
    3: "Дніпропетровська",
    4: "Донецька",
    5: "Житомирська",
    6: "Закарпатська",
    7: "Запорізька",
    8: "Івано-Франківська",
    9: "Київська",
    10: "Кіровоградська",
    11: "Луганська",
    12: "Львівська",
    13: "Миколаївська",
    14: "Одеська",
    15: "Полтавська",
    16: "Рівенська",
    17: "Сумська",
    18: "Тернопільська",
    19: "Харківська",
    20: "Херсонська",
    21: "Хмельницька",
    22: "Черкаська",
    23: "Чернівецька",
    24: "Чернігівська",
    25: "Республіка Крим"
}

eng_idx = {
    1: "Cherkasy",
    2: "Chernihiv",
    3: "Chernivtsi",
    4: "Crimea",
    5: "Dnipropetrovs'k",
    6: "Donets'k",
    7: "Ivano-Frankivs'k",
    8: "Kharkiv",
    9: "Kherson",
    10: "Khmel'nyts'kyy",
    11: "Kiev",
    12: "Kiev City", # Assuming it is a part of Kiev, ignorig it
    13: "Kirovohrad",
    14: "Luhans'k",
    15: "L'viv",
    16: "Mykolayiv",
    17: "Odessa",
    18: "Poltava",
    19: "Rivne",
    20: "Sevastopol'", # Assuming it is a part of Crimea, ignoring it
    21: "Sumy",
    22: "Ternopil'",
    23: "Transcarpathia",
    24: "Vinnytsya",
    25: "Volyn",
    26: "Zaporizhzhya",
    27: "Zhytomyr",
}

eng_to_ukr = {
    1: 22,
    2: 24,
    3: 23,
    4: 25,
    5: 3,
    6: 4,
    7: 8,
    8: 19,
    9: 20,
    10: 21,
    11: 9,
    13: 10,
    14: 11,
    15: 12,
    16: 13,
    17: 14,
    18: 15,
    19: 16,
    21: 17,
    22: 18,
    23: 6,
    24: 1,
    25: 2,
    26: 7,
    27: 5
}


def rename_regions(input_dir, output_dir):
    data_files = Path(input_dir).glob('*.csv')
    for filename in data_files:
        input_file = open(filename, 'r')
        line = input_file.readline()
        m = REGION_RE.match(line)
        if m is None:
            raise LookupError('Region index is not found in file {}'.format(filename))
        eng_idx = int(m.group(1))
        if eng_idx not in eng_to_ukr:
            continue
        ukr_idx = eng_to_ukr[eng_idx]
        filename_elements = filename.name.split('_')
        filename_elements[2] = str(ukr_idx)

        output_filename = OUTPUT_FILENAME_FORMAT.format(output_dir, '_'.join(filename_elements))
        line = REPLACE_REGION_RE.sub(r'\g<reg>{}'.format(ukr_idx), line)

        with open(output_filename, 'w') as f:
            f.write(line)
            for line in input_file.readlines():
                f.write(line)
        input_file.close()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        input_dir = Path(sys.argv[1])
        if input_dir.exists():
            output_dir = Path(DATA_DIR_FORMAT.format(Path.cwd()))
            if not output_dir.exists():
                output_dir.mkdir()
            rename_regions(input_dir, output_dir)
    else:
        print('Usage: {} <directory with data files>'.format(sys.argv[0]))
