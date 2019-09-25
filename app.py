import dash
import dash_core_components as dcc
import dash_html_components as html 

app = dash.Dash()

app.layout = html.Div(children = [
    html.H1(children='Temporary Graph'),
    dcc.Graph(
        id='temp',
        figure={
            'data': [
                {
                    'x': [1,2,3,4,5],
                    'y': [7,4,7,5,6],
                    'type': 'line',
                    'name': 'first graph'
                },
                {
                    'x': [1, 2, 3, 4, 5],
                    'y': [2, 6, 8, 3, 5],
                    'type': 'bar',
                    'name': 'second graph'
                }
            ],

            'layout': {
                'title': 'First Web App Setup'
            }
        }
    )
])

if __name__ == '__main__': 
    app.run_server(debug=True)
