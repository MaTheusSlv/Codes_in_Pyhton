#App Hello world em Plotly

# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import dash_bootstrap_components as dbc

# Initialize the app
external_stylesheets = [dbc.themes.CERULEAN] #incorporate a Dash Bootstrap theme
app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout
app.layout = dbc.Container([
    dbc.Row([
        html.Div('Olá Mundo!', style={'textAlign': 'center', 'font-size':'30px', 'color':'white', 'background-color': 'grey'})
        ])
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
