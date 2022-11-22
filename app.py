from spyre import server
from query import DATA_DIR_FORMAT, UKR_IDX
from pathlib import Path
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np

def replace_year(x):
    print(type(x))
    return x


class VHIApp(server.App):
    title = "Vegetation Health Index"

    inputs = [
        {
            "type": 'dropdown',
            "label": 'VH type',
            "options": [
                {"label": "VCI", "value": "VCI"},
                {"label": "TCI", "value": "TCI"},
                {"label": "VHI", "value": "VHI"}
            ],
            "key": 'vh',
            "action_id": "update_data"
        },
        {
            "type": 'dropdown',
            "label": 'Region',
            "options": None,
            "value": '1',
            "key": 'region',
            "action_id": "update_data"
        }]

    controls = [
        {
            "type": "hidden",
            "id": "update_data"
        }]

    tabs = ["Plot", "Table"]

    outputs = [
        {
            "type": "plot",
            "id": "plot",
            "control_id": "update_data",
            "tab": "Plot"
        },
        {
            "type": "table",
            "id": "table_id",
            "control_id": "update_data",
            "tab": "Table",
            "on_page_load": True
        }
    ]

    def getData(self, params):
        print('getData params = {}'.format(params))
        idx = params['region']
        data_glob = Path(data_dir).glob('vhi_id_{}_*.csv'.format(idx))
        for data_file in data_glob:
            df = pd.read_csv(data_file, index_col=False, header=1)
        df = df[['year', 'week', params['vh']]]
        return df

    def getPlot(self, params):
        df = self.getData(params).drop(['week'], axis=1)
        df = df.groupby('year', as_index=False)[params['vh']].mean()
        plt_obj = df.plot(x='year', y=params['vh'])
        plt_obj.set_ylabel(params['vh'])
        plt_obj.set_xlabel("Year")
        plt_obj.set_title('Average {}'.format(params['vh']))
        return plt_obj.get_figure()


def run_server(data_dir: str):
    options = list()
    for name, idx in UKR_IDX.items():
        options.append({"label": name, "value": str(idx)})
    app = VHIApp()
    app.inputs[1]["options"] = options
    app.launch()


if __name__ == '__main__':
    data_dir = Path(DATA_DIR_FORMAT.format(Path.cwd()))
    if data_dir.exists():
        run_server(data_dir)
    else:
        print('Data dir {} does not exists'.format(data_dir))

