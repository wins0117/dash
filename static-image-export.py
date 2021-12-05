from base64 import b64encode

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
from numpy.random import seed, rand
import numpy as np
import os 
# Generate random data
np.random.seed(1)
x, y, sz, cl = np.random.rand(4, 100)
fig = px.scatter(x=x, y=y, size=sz, color=cl)

app = dash.Dash(__name__)


app.layout = html.Div([
    html.P("Render Option:"),
    dcc.RadioItems(
        id='render-option',
        options=[{'value': x, 'label': x} 
                 for x in ['interactive', 'image']],
        value='image'
    ),
    html.Div(id='output'),
])


@app.callback(
    Output("output", "children"), 
    [Input('render-option', 'value')])
def display_graph(render_option):
    if render_option == 'image':
        img_bytes = fig.to_image(format="png")
        encoding = b64encode(img_bytes).decode()
        img_b64 = "data:image/png;base64," + encoding
        return html.Img(src=img_b64, style={'width': '100%'})
    else:
        return dcc.Graph(figure=fig)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run_server(host = "0,0,0,0", port = port)
