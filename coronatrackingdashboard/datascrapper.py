import requests
from bs4 import BeautifulSoup

from datawrangling import *


def scrape_corona_data():
    """This function scrapes the data from the target website and returns a well formatted dict that contains information about every given country."""
    from collections import (
        defaultdict,
    )  # Importing the defaultdict model, that will be used to store the information while scraping the website

    countries_data = defaultdict(dict)
    coronameter = requests.get(
        "https://www.worldometers.info/coronavirus/"
    )  # requesting the index page from the server, it is also where our information resides
    bscorona = BeautifulSoup(
        coronameter.text, "lxml"
    )  # parsing the webpage to a beautifulsoup object.
    corona_table = bscorona.find(
        "table", id="main_table_countries_today"
    )  # selecting the table where our data is contained.
    column_names = get_column_names(corona_table.tr.text)
    for tr in corona_table.find_all("tr", {"style": ""})[2:-2]:
        line = get_country_data(tr.text)
        countries_data[line[0]] = dict(zip(column_names, line[1:]))
    return create_clean_dataframe(countries_data)
