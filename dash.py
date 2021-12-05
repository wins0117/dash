
from dash import html , Dash
from dash import dcc

from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import  os 

df = pd.read_csv("台鐵列車準點率.csv")
df["準點率"] = df["準點率"].astype("float")
all_cars = df["車種"].unique()
app = Dash(__name__)

app.layout = html.Div([

    dcc.Graph(id="line-chart"),
    dcc.Checklist(
        id="checklist",
        options=[{"label": x, "value": x} 
                 for x in all_cars],
        value=all_cars[3:],
        labelStyle={'display': 'inline-block'}
    )
])

@app.callback(
    Output("line-chart", "figure"), 
    [Input("checklist", "value")])
def update_line_chart(car):
    mask = df["車種"].isin(car)
    fig = px.line(df[mask], 
        x="月份", y="準點率", color='線別')
    return fig

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run_server(host = "127.0.0.1", port=port)