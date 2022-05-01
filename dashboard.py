<<<<<<< HEAD:dashboard.py
import dash
import dash_html_components as html
import plotly.graph_objects as go
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd

data = pd.read_csv('pos_sales.csv')
app = dash.Dash()

monthly = data.groupby('month')['profit'].sum().to_frame()
daily = data.groupby('dayofweek')['profit'].sum().to_frame()
app = dash.Dash()

server = app.server




app.layout = html.Div(id = 'parent', children = [
    html.H1(id = 'H1', children = 'BI_dasboard', style = {'textAlign':'center',\
                                            'marginTop':40,'marginBottom':40}),

        dcc.Dropdown( id = 'dropdown',
        options = [
            {'label':'month', 'value':'M' },
            {'label': 'dayofweek', 'value':'D'},
            ],
        value = 'M'),
        dcc.Graph(id = 'bar_plot')
    ])
    
    
@app.callback(Output(component_id='bar_plot', component_property= 'figure'),
              [Input(component_id='dropdown', component_property= 'value')])
def graph_update(dropdown_value):
    print(dropdown_value)
    fig = px.Figure([px.bar(data ,x = data['profit'], y = data['{}'.format(dropdown_value)],\
                     line = dict(color = 'firebrick', width = 4))
                     ])
    
    fig.update_layout(title = 'Dash board',
                      xaxis_title = 'Profit made',
                      yaxis_title = 'Time Frame'
                      )
    return fig  



if __name__ == '__main__': 
    app.run_server()
=======
import dash
from dash import html

from dash import dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd

data = pd.read_csv('pos_sales.csv')
<<<<<<< HEAD
app = dash.Dash(__name__)
=======
monthly = data.groupby('month')['profit'].sum().to_frame()
daily = data.groupby('dayofweek')['profit'].sum().to_frame()
app = dash.Dash()
>>>>>>> 1aed93075b0facd3c8dcb0c19eec93ebe7a6c5c1
server = app.server




app.layout = html.Div(id = 'parent', children = [
    html.H1(id = 'H1', children = 'BI_dasboard', style = {'textAlign':'center',\
                                            'marginTop':40,'marginBottom':40}),

        dcc.Dropdown( id = 'dropdown',
        options = [
            {'label':'Monthly', 'value':'M' },
            {'label': 'daily', 'value':'D'},
            ],
        value = 'M'),
        dcc.Graph(id = 'bar_plot')
    ])
    
    
@app.callback(Output(component_id='bar_plot', component_property= 'figure'),
              [Input(component_id='dropdown', component_property= 'value')])
def graph_update(dropdown_value):
    print(dropdown_value)
    fig = px.Figure([px.bar(data ,x = data['month'], y = data['{}'.format(dropdown_value)],\
                     line = dict(color = 'firebrick', width = 4))
                     ])
    
    fig.update_layout(title = 'Stock prices over time',
                      xaxis_title = 'Month',
                      yaxis_title = 'Profit'
                      )
    return fig  



if __name__ == '__main__': 
    app.run_server()
>>>>>>> c65f91903a5f3b67a64a4ac2b669a2370ede608f:dasboard.py
