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
        up_time = items.find("span", class_="featured")
        location = items.find("span", class_="region")
        if(company and up_time):
            jobs = {
                "company": company.string,
                "upTime": up_time.string,
                "location": location.string
            }
        wwr_jobs.append(jobs)
    return wwr_jobs
