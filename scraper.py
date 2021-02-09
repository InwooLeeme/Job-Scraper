import requests
from bs4 import BeautifulSoup

wwr_url = "https://weworkremotely.com/remote-jobs/search?term=python"


def extract_wwr():
    wwr_jobs = []
    r = requests.get(wwr_url)
    html = BeautifulSoup(r.text, "html.parser")
