
import dash
from dash import html

from dash import dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd

data = pd.read_csv('pos_sales.csv')

app = dash.Dash(__name__)

#monthly = data.groupby('month')['profit'].sum().to_frame()
#daily = data.groupby('dayofweek')['profit'].sum().to_frame()
app = dash.Dash()

server = app.server




app.layout = html.Div([
    html.H4('Profits by day of week'),
    dcc.Dropdown(
        id="dropdown",
        options=["Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturday","Sunday" ],
        value="0",
        clearable=False,
    ),
    dcc.Graph(id="graph"),
])
app.layout = html.Div([
    html.H4('Profits by month'),
    dcc.Graph(id="graph"),
])
    
    
@app.callback(
    Output("graph", "figure"), 
    Input("dropdown", "value"))
def update_bar_chart(dayofweek):
    mask = data["dayofweek"] == dayofweek
    fig1 = px.bar(data[mask] ,  x = 'profit' , y = 'dayofweek' , color = 'year' , title = 'daily profit ' )
    fig1.show()
    return fig1

@app.callback(
    Output("graph", "figure"), 
    Input("dropdown", "value"))
def update_bar_chart(month):
    fig1 = px.bar(data[mask] ,  x = 'profit' , y = 'month' , color = 'year' , title = 'monthly profit ' )
    fig1.show()
    return fig1



if __name__ == '__main__': 
    app.run_server()

