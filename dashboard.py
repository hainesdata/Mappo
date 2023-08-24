import pandas as pd
from dash import Dash, html, dash_table


class Dashboard:
    def __init__(self):
        self.app = Dash(__name__)
        self.data = None

    def load_data(self, path):
        print('Importing data...')
        self.data = pd.read_csv(path)
        print('Data imported successfully.\n')

    def add_layout(self):
        self.load_data('._data')
        self.app.layout = html.Div([
            html.Div(children='My First App with Data'),
            dash_table.DataTable(data=self.data.to_dict('records'))
        ])

    def start(self):
        self.add_layout()
        self.app.run(debug=True)


import plotly.figure_factory as ff
import plotly.express as px

class Map:
    def __init__(self, parent):
        self.parent = parent
        self.ff_instance = None
        self.data = None

    def load_map(self):
        self.ff_instance = ff.create_hexbin_mapbox(
            data_frame=self.parent.data,
            lat='lat',
            lon='long',
            nx_hexagon=10,
            opacity=0.6,
            labels={'color': 'Point Count'},
        )

        # TODO: Implement bounds and formatting
        # self.ff_instance.update_layout(margin=dict(b=0, t=0, l=0, r=0))