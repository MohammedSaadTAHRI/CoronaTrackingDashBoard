Heroku link : https://coronameterdashboard.herokuapp.com/
# CoronaMeterDashBoard


<h4 align="center">A DashBoard that keeps you updated  (COVID19)</h4>

CoronaMeterDashBoard is a web app that tracks Corona cases by scraping https://www.worldometers.info/coronavirus/.
It is a project, or rather a prototype build during a class in my university to learn webscraping and deployment using all the tools stated down below.
It is deployed on heruko. Its main objective is to keep you up to date on the latest COV19 news via nice and modern visualizations. 

## Visit it

### SnapShot
![A snapshot of the web application](https://github.com/MohammedSaadTAHRI/CoronaTrackingDashBoard/blob/main/imgs/snapshot.PNG)

### Link
[FR]: https://coronameterdashboard.herokuapp.com/
https://coronameterdashboard.herokuapp.com/


## Features

- [x] Cross-platform
- [x] Awesome Viz
- [x] No singup/login required

## Code
`datascrapper.py` contains the requests and BS code that scrapes the website.
`datawrangling.py` contains the code to format the scrapped data.
`figureplots.py` contains the code that builds the plotly figures.
`dashboard.py` contains the code builds the app and utilizes all the other modules.

## Built with
- [Requests](https://requests.readthedocs.io/en/master/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Plotly](https://plotly.com/python/)
- [Dash](https://plotly.com/dash/)

## Setup
Clone this repo to your desktop or a specific folder you want to run the project on, run `pip install -r requirements.txt` to install all the dependencies.
You might want to create a virtual environment before installing the dependencies.

To run the project on your localhost, you can use `python dashboard.py` and it will launch on your localhost via the port 8050.

## Deployement
To deploy your version of the project, you can directly use your git repo to link it with Heroku, Heroku will take care of the rest.

## License

No license
