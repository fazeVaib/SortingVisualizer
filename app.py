import dash
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input, Output
import time 
import plotly.graph_objects as go

app = dash.Dash()

app.title = "Sorting Visualizer"

data = [2,6,4,7,8,4,5,7,8,9,4]

app.layout = html.Div(children = [
    html.H1(children='Sorting Visualizer'),
    dcc.Input(id='input', value= 1, type='number'),
    dcc.Graph(id='graph'),
    dcc.Interval(id='graph-interval', interval=300, n_intervals=0),
    html.Div(id='test-div')
])

f = 9
def testfunc(ignore): 
    global f 
    f + f+1
    return "Function i called {} times.".format(str(f))

for i in range(10): 
    time.sleep(2)
    app.callback(
        Output('test-div', 'children'),
        [Input('input', 'value')]
    )(testfunc)


# @app.callback(
#     Output(component_id='graph', component_property='figure'),
#     [Input('graph-interval', 'n_intervals')])
# def updateValue(n):
#     global data
#     try:
#         new_data = [n*x for x in data]
#     except Exception:
#         new_data = [20 for x in data]

#     d = [go.Bar(y=new_data)]
#     layout = {'yaxis': {'showgrid': False,
#                         'showticklabels': False,
#                         'zeroline': False,
#                         'range': [0,500] 
#                         },
#               'xaxis': {'showgrid': False,
#                         'zeroline': False,
#                         'showticklabels': False,
#                         'title': 'Number of operations: 0'},
#               'plot_bgcolor': 'rgba(0,0,0,0)',
#               'title': str(n) + ' Visualization'}

#     fig = go.FigureWidget(d, layout)
#     return fig



if __name__ == '__main__': 
    app.run_server(debug=True)

