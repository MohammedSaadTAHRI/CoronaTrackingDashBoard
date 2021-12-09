# import plotly.offline as pyo
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from figureplots import *
from datascrapper import scrape_corona_data

# Initialize the scrapping process and the figures
countries_data = scrape_corona_data()
init_continent_fig, init_k_countries_plot, init_box_fig = init_figures(countries_data)

# Building the app
app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(
    [
        html.H1(
            "Corona Tracker DashBoard",
            style={
                "text-align": "center",
                "padding-top": "10px",
                "color": "#1387C4",
            },
        ),
        html.Br(),
        html.Div(
            [
                html.Br(),
                html.H2(
                    "Corona Cases/Recovered/Deaths by Continent",
                    style={
                        "text-align": "center",
                        "background-color": "#D4CED6",
                        "height": "50px",
                        "padding-top": "20px",
                    },
                ),
                html.Br(),
                dcc.Dropdown(
                    id="select_keyword",
                    options=[
                        dict(label="Today's Data", value="New"),
                        dict(label="Total Data", value="Total"),
                    ],
                    multi=False,
                    value="New",
                    style={"width": "40%"},
                ),
                dcc.Graph(id="continent_corona_bar", figure=init_continent_fig),
            ]
        ),
        html.Div(
            [
                html.Br(),
                html.H2(
                    "Visualize Countries by attribute.",
                    style={
                        "text-align": "center",
                        "background-color": "#D4CED6",
                        "height": "50px",
                        "padding-top": "20px",
                    },
                ),
                html.Br(),
                dcc.Dropdown(
                    id="select_attribute",
                    options=[
                        dict(label="Total Cases", value="TotalCases"),
                        dict(label="New Cases", value="NewCases"),
                        dict(
                            label="Total Cases per 1M population",
                            value="Tot Cases/1M pop",
                        ),
                        dict(label="Active Cases", value="ActiveCases"),
                        dict(
                            label="Serious, Critical Cases",
                            value="Serious,Critical",
                        ),
                        dict(label="Total Deaths", value="TotalDeaths"),
                        dict(label="New Deaths", value="NewDeaths"),
                        dict(
                            label="Deaths per 1M population",
                            value="Deaths/1M pop",
                        ),
                        dict(label="Total Recovered", value="TotalRecovered"),
                        dict(label="New Recovered", value="NewRecovered"),
                        dict(label="Total Tests", value="TotalTests"),
                        dict(
                            label="Tests per 1M population",
                            value="Tests/1M pop",
                        ),
                    ],
                    multi=False,
                    value="TotalCases",
                    style={"width": "60%", "display": "inline-block"},
                ),
                dcc.Dropdown(
                    id="select_k_countries",
                    options=[
                        dict(label="Top 5", value=5),
                        dict(label="Top 10", value=10),
                        dict(label="Top 25", value=25),
                        dict(label="Top 50", value=50),
                    ],
                    multi=False,
                    value=10,
                    style={"width": "30%", "display": "inline-block"},
                ),
                dcc.Graph(id="k_countries_sorted", figure=init_k_countries_plot),
            ]
        ),
        html.Div(
            [
                html.Br(),
                html.H2(
                    "BoxPlot to explain the distribution of the variables",
                    style={
                        "text-align": "center",
                        "background-color": "#D4CED6",
                        "height": "50px",
                        "padding-top": "20px",
                    },
                ),
                html.Br(),
                dcc.Dropdown(
                    id="select_box_attribute",
                    options=[
                        dict(
                            label="Deaths per 1M population",
                            value="Deaths/1M pop",
                        ),
                        dict(
                            label="Tests per 1M population",
                            value="Tests/1M pop",
                        ),
                    ],
                    multi=False,
                    value="Deaths/1M pop",
                    style={"width": "40%"},
                ),
                dcc.Graph(id="continent_box_plot", figure=init_box_fig),
            ]
        ),
    ]
)


@app.callback(
    Output("continent_corona_bar", "figure"), Input("select_keyword", "value")
)
def update_continent_corona_bar(value):
    return plot_continent_data(data, keyword=value)


@app.callback(
    Output("k_countries_sorted", "figure"),
    Input("select_attribute", "value"),
    Input("select_k_countries", "value"),
)
def update_k_countries_sorted(attribute, n_countries):
    return plot_top_k_countries(data, n_countries, attribute)


@app.callback(
    Output("continent_box_plot", "figure"),
    Input("select_box_attribute", "value"),
)
def update_continent_box_plot(value):
    return plot_boxplots(data, keyword=value)


if __name__ == "__main__":
    data = scrape_corona_data()
    app.run_server()
