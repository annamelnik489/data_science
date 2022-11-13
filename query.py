from pathlib import Path
import pandas as pd

DATA_DIR_FORMAT='{}/data_2'

UKR_IDX = {
    "Вінницька": 1,
    "Волинська": 2,
    "Дніпропетровська": 3,
    "Донецька": 4,
    "Житомирська": 5,
    "Закарпатська": 6,
    "Запорізька": 7,
    "Івано-Франківська": 8,
    "Київська": 9,
    "Кіровоградська": 10,
    "Луганська": 11,
    "Львівська": 12,
    "Миколаївська": 13,
    "Одеська": 14,
    "Полтавська": 15,
    "Рівенська": 16,
    "Сумська": 17,
    "Тернопільська": 18,
    "Харківська": 19,
    "Херсонська": 20,
    "Хмельницька": 21,
    "Черкаська": 22,
    "Чернівецька": 23,
    "Чернігівська": 24,
    "Республіка Крим": 25
}

def query_drought(data_dir, region_name, max_vhi, min_vhi):
    data_glob = Path(data_dir).glob('vhi_id_{}_*.csv'.format(UKR_IDX[region_name]))
    for data_file in data_glob:
        df = pd.read_csv(data_file, index_col=False, header=1)
        print('Region: {}, {}% <= VHI < {}%:'.format(region_name, min_vhi, max_vhi))
        print(df[(df['VHI']<float(max_vhi)) & (df['VHI']>=float(min_vhi))][['year', 'week', 'VHI']])
