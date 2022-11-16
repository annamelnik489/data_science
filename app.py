from spyre import server
from query import DATA_DIR_FORMAT, UKR_IDX
from pathlib import Path

# from get_data import download_region


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
            "options": [
                {"label": "Cherkasy", "value": "1"},
                {"label": "Chernihiv", "value": "2"},
                {"label": "Chernivtsi", "value": "3"},
                {"label": "Crimea", "value": "4"},
                {"label": "Dnipropetrovs'k", "value": "5"},
                {"label": "Donets'k", "value": "6"},
                {"label": "Ivano-Frankivs'k", "value": "7"},
                {"label": "Kharkiv", "value": "8"},
                {"label": "Kherson", "value": "9"},
                {"label": "Khmel'nyts'kyy", "value": "10"},
                {"label": "Kiev", "value": "11"},
                {"label": "Kirovohrad", "value": "13"},
                {"label": "Luhans'k", "value": "14"},
                {"label": "L'viv", "value": "15"},
                {"label": "Mykolayiv", "value": "16"},
                {"label": "Odessa", "value": "17"},
                {"label": "Poltava", "value": "18"},
                {"label": "Rivne", "value": "19"},
                {"label": "Sumy", "value": "21"},
                {"label": "Ternopil'", "value": "22"},
                {"label": "Transcarpathia", "value": "23"},
                {"label": "Vinnytsya", "value": "24"},
                {"label": "Volyn", "value": "25"},
                {"label": "Zaporizhzhya", "value": "26"},
                {"label": "Zhytomyr", "value": "27"}],
            "value": '1',
            "key": 'region',
            "action_id": "update_data"
        }]
    controls = [{"type": "hidden",
                "id": "update_data"}]

    tabs = ["Plot", "Table"]

    # outputs = [
    #     {
    #         "type": "table",
    #         "id": "table_id",
    #         "control_id": "update_data",
    #         "tab": "Table",
    #         "on_page_load": True
    #     }
    # ]

    # def getData(self, params):
    #     ticker = params['ticker']
    #     if ticker == 'empty':
    #         ticker = params['custom_ticker'].upper()

    #     xchng = "NASD"
    #     param = {
    #         'q': ticker,  # Stock symbol (ex: "AAPL")
    #         'i': "86400",  # Interval size in seconds ("86400" = 1 day intervals)
    #         'x': xchng,  # Stock exchange symbol on which stock is traded (ex: "NASD")
    #         'p': "3M"  # Period (Ex: "1Y" = 1 year)
    #     }
    #     df =  download_region(param)
    #     return df

    # def getPlot(self, params):
    #     df = self.getData(params).drop(['Volume'], axis=1)
    #     plt_obj = df.plot()
    #     plt_obj.set_ylabel("Price")
    #     plt_obj.set_xlabel("Date")
    #     plt_obj.set_title(params['ticker'])
    #     return plt_obj.get_figure()


def run_server(data_dir:str):
    options = list()
    for name, idx in UKR_IDX:
        options.append({"label":name, "value":str(idx)})
    app = VHIApp(options)
    app.launch()

if __name__ == '__main__':
    data_dir = Path(DATA_DIR_FORMAT.format(Path.cwd()))
    if data_dir.exists():
        run_server(data_dir)
    else:
        print('Data dir {} does not exists'.format(data_dir))
