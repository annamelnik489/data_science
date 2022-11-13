#!/usr/bin/env python

import sys
from pathlib import Path
import pandas as pd
from query import DATA_DIR_FORMAT, UKR_IDX

def query_data(data_dir, region_name, year):
    data_glob = Path(data_dir).glob('vhi_id_{}_*.csv'.format(UKR_IDX[region_name]))
    for data_file in data_glob:
        df = pd.read_csv(data_file, index_col=False, header=1)
        year_df = df[(df['year']==int(year)) & (df['VHI']!=-1)]
        print('Region: {}, year {}, max:'.format(region_name, year))
        print(year_df[(year_df['VHI']==year_df['VHI'].max())][['year', 'week', 'VHI']])
        print('Region: {}, year {}, min:'.format(region_name, year))
        print(year_df[(year_df['VHI']==year_df['VHI'].min())][['year', 'week', 'VHI']])

if __name__ == '__main__':
    if len(sys.argv) == 3:
        data_dir = Path(DATA_DIR_FORMAT.format(Path.cwd()))
        if data_dir.exists():
            query_data(data_dir, sys.argv[1], sys.argv[2])
        else:
            print('Data dir {} does not exists'.format(data_dir))
    else:
        print('Usage: {} <region_name> <year>'.format(sys.argv[0]))

