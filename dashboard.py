import pandas as pd
from dash import Dash, html, dash_table


class Dashboard:
    def __init__(self):
        self.app = Dash(__name__)
        self.data = None

    def load_data(self, path):
        print('Importing data...')
        self.data = pd.read_table(path)
        print('Data imported successfully.\n')

    def add_layout(self):
        self.app.layout = html.Div([
            html.Div(children='My First App with Data'),
            dash_table.DataTable(data=self.data.to_dict('records'), page_size=10)
        ])

    def start(self):
        print('Starting Dash app...')
        self.add_layout()
        self.app.run(debug=True)
