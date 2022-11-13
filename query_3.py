#!/usr/bin/env python

import sys
from pathlib import Path
from query import DATA_DIR_FORMAT, query_drought

if __name__ == '__main__':
    if len(sys.argv) == 2:
        data_dir = Path(DATA_DIR_FORMAT.format(Path.cwd()))
        if data_dir.exists():
            query_drought(data_dir, sys.argv[1], 35, 15)
        else:
            print('Data dir {} does not exists'.format(data_dir))
    else:
        print('Usage: {} <region_name>'.format(sys.argv[0]))

