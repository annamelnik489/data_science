from spyre import server
# from get_data import download_region

class SimpleApp(server.App):
    title="Vegetation Health Index"

    inputs = [
    {
        "type": 'dropdown',
        "label": 'Region',
        "options": [
        ]
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
        "key": 'ticker',
        "action_id": "update_data"
    }]
    controls = [{
        "type": "button",
        "id": "update_data",
        "label": "get "
    }]

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




app = SimpleApp()
app.launch()
