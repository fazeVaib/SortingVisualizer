import dash
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input, Output

app = dash.Dash()

app.title = "Sorting Visualizer"

data = [2,6,4,7,8,4,5,7,8,9,4]

app.layout = html.Div(children = [
    html.H1(children='Sorting Visualizer'),
    dcc.Input(id='input', value= 1, type='number'),
    dcc.Graph(
        id='graph',
        figure={
            'data': [
                {
                    'y': data,
                    'type': 'bar',
                    'name': 'first graph'
                }
            ],
            
            'layout': {
                'title': 'Visualization',
                'yaxis': {
                    'range': [0, 1000]
                }
            }
        }
    )
])

@app.callback(
    Output(component_id = 'graph', component_property='figure'),
    [Input(component_id='input', component_property='value')]
)
def updateValue(n):
    global data
    try: 
        new_data = [ i*n for i in data]
    except Exception: 
        new_data = [i for i in data] 

    return {
            'data': [
                {
                    'y': new_data,
                    'type': 'bar',
                    'name': 'first graph'
                }
            ],
            'layout': {
                'title': 'Visualization',
                'yaxis': {
                    'range': [0, 1000]
                }
            }
        }


if __name__ == '__main__': 
    app.run_server(debug=True)
