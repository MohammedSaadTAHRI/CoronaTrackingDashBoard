import plotly.graph_objs as go


def plot_continent_data(data, keyword):
    """
    This function creates a Figure from continental data.

    Parameters:
        data : dataframe
            The whole dataset.
        keyword : str
            The keyword used to define the figure wanted, the available keyword : {"Total", "New"}

    Returns:
        fig : Figure
            The figure that will be drawed on plotly.
    """
    if keyword == "New":
        cols = ["NewCases", "NewRecovered", "NewDeaths"]
    else:
        cols = ["TotalCases", "TotalRecovered", "TotalDeaths"]
    res = data.groupby("Continent")[cols].sum()

    plot_data = []
    colors = ["LightSkyBlue", "#01D000", "#D00000"]
    for col, color in zip(cols, colors):
        plot_data.append(
            go.Bar(
                x=res.index.to_list(),
                y=res[col],
                name=col,
                marker=dict(color=color),
            )
        )

    layout = go.Layout(
        title=f"Corona {keyword} Cases/Recovered/Deaths",
        xaxis=dict(title="Continents"),
        yaxis=dict(title="Cases per Continent"),
    )

    fig = go.Figure(data=plot_data, layout=layout)
    return fig


def get_continent_sorted_data(data, continent, sortedby="TotalCases", ascending=False):
    """
    This function creates a sorted dataframe related to a continent and sorted by a columns.

    Parameters:
        data : dataframe
            The whole dataset.
        continent : str
            The continent we want to get the data from.
        sortedby : str, Default="TotalCases"
            The name of the column we want to sort by.
        ascending : Boolean, Default=False
            Either we want to sort in an ascending order or descending order.
    Returns:
        groupedbydata : dataframe
            A dataframe groupedby the continent.
    """
    return (
        data.groupby("Continent")
        .get_group(continent)
        .sort_values(by=sortedby, ascending=ascending)
        .reset_index()
    )


def get_top_k_countries(data, k_countries=10, sortedby="TotalCases", ascending=False):
    """
    This function creates a k-len dataframe sorted by a key.

    Parameters:
        data : dataframe.
            The whole dataset.
        k_countries : int, Default=10
            The number of countries you want to plot.
        sortedby : str, Default="TotalCases".
            The column name we want to sort the data by
        ascending : Boolean, Default=False
            Either we want to sort in an ascending order or descending order.

    Returns:
        data : dataframe
            The k_contries lines dataframe sortedby the key given and in the wanted order.
    """
    return data.sort_values(by=sortedby, ascending=ascending).iloc[:k_countries]


def plot_top_k_countries(data, n_countries, sortby):
    """This function returns a figure where a number of countries are sorted by the value that resides in sortby."""
    res = get_top_k_countries(data, n_countries, sortby)
    plot_data = []

    plot_data.append(go.Bar(x=res.index.to_list(), y=res[sortby], name=sortby))

    layout = go.Layout(
        title=f"Top Countries orderedby {sortby}",
        xaxis=dict(title="Countries"),
        yaxis=dict(title=f"{sortby}"),
    )

    fig = go.Figure(data=plot_data, layout=layout)
    return fig


def plot_boxplots(data, keyword="Deaths/1M pop"):
    """This function returns a figure of the boxplot related to each continent in regards to the keyword."""
    plot_data = []
    grouped_data = data.groupby("Continent")
    continents = data["Continent"].value_counts().index.to_list()
    for continent in continents:
        plot_data.append(
            go.Box(y=grouped_data.get_group(continent)[keyword], name=continent)
        )
    layout = go.Layout(
        title=f"Boxplots using {keyword}",
        xaxis=dict(title="Continents"),
        yaxis=dict(title=f"{keyword}"),
    )
    fig = go.Figure(data=plot_data, layout=layout)
    return fig


def init_figures(data):
    "This function initiate all the needed figure to start the app."
    return (
        plot_continent_data(data, keyword="New"),
        plot_top_k_countries(data, 10, "TotalCases"),
        plot_boxplots(data),
    )
