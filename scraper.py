import requests
from bs4 import BeautifulSoup

wwr_url = "https://weworkremotely.com/remote-jobs/search?term=python"


def extract_wwr():
    wwr_jobs = []
    r = requests.get(wwr_url)
    html = BeautifulSoup(r.text, "html.parser")
    section = html.find(
        "div", class_="jobs-container").find("section", class_="jobs")
    article = section.find("article")
    li = article.find("ul").find_all("li")
    for items in li:
        company = items.find("span", class_="company")
        print(company)
