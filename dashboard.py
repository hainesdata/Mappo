import time
import pandas as pd
from dash import Dash, html, dash_table, dcc
import plotly.figure_factory as ff
import plotly.express as px


class Dashboard:
    def __init__(self):
        self.app = Dash(__name__)
        self.data = None

    def load_data(self, path):
        for i in range(10):
            buffer = 0.5
            print('\rImporting data', end='', flush=True)
            time.sleep(buffer)
            print('\rImporting data.', end='', flush=True)
            time.sleep(buffer)
            print('\rImporting data..', end='', flush=True)
            time.sleep(buffer)
            print('\rImporting data...', end='', flush=True)
            time.sleep(buffer)

        self.data = pd.read_csv(path)
        print('Data imported successfully.\n')

    def add_layout(self):
        self.load_data('._data')
        map_object = Map(self)
        map_object.load_map()

        self.app.layout = html.Div([
            html.Div(children='Mappo Heat'),
            dcc.Graph(figure=map_object.map_instance)
        ])

    def start(self):
        self.add_layout()
        self.app.run(debug=True)


class Map:
    def __init__(self, parent):
        self.parent = parent
        self.ff_instance = None
        self.map_instance = None
        self.data = None

    def load_map(self):
        self.map_instance = px.density_mapbox(self.parent.data,
                                              lat='lat',
                                              lon='lon',
                                              radius=10,
                                              mapbox_style='open-street-map'
                                              )

        # TODO: Make zones based on density
        #
        # self.map_instance = ff.create_hexbin_mapbox
        #     data_frame=self.parent.data,
        #     lat='lat',
        #     lon='lon',
        #     nx_hexagon=10,
        #     opacity=0.6,
        #     labels={'color': 'Point Count'},
        #     min_count=1
        # )

        # self.ff_instance.update_layout(margin=dict(b=0, t=0, l=0, r=0))