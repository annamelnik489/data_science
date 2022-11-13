#!/usr/bin/env python

import sys
import requests
from datetime import datetime
from pathlib import Path


URL_FORMAT='https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?provinceID={}&country=UKR&yearlyTag=Weekly&type=Mean&TagCropland=WHEA&year1=1982&year2=2022'
DATA_DIR_FORMAT='{}/raw_data'
FILENAME_FORMAT = '{}/vhi_id_{}_{}-{}-{}_{}-{}.csv'

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
    13: "Kirovohrad",
    14: "Luhans'k",
    15: "L'viv",
    16: "Mykolayiv",
    17: "Odessa",
    18: "Poltava",
    19: "Rivne",
    21: "Sumy",
    22: "Ternopil'",
    23: "Transcarpathia",
    24: "Vinnytsya",
    25: "Volyn",
    26: "Zaporizhzhya",
    27: "Zhytomyr",
}

def download_region(region_idx, data_dir):
    url = URL_FORMAT.format(region_idx)
    response = requests.get(url)
    if response.status_code == 200:
        now = datetime.now()
        filename = FILENAME_FORMAT.format(data_dir, region_idx, now.year, now.month, now.day, now.hour, now.minute)
        with open(filename, 'wb') as f:
            f.write(response.content)


if __name__ == '__main__':
    data_dir = Path(DATA_DIR_FORMAT.format(Path.cwd()))
    if not data_dir.exists():
        data_dir.mkdir()
    for idx in eng_idx:
        print('Downloading {}'.format(eng_idx[idx]))
        download_region(idx, data_dir)
