import requests
from bs4 import BeautifulSoup

wwr_url = "https://weworkremotely.com/remote-jobs/search?term=python"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


def extract_wwr():
    wwr_jobs = []
    r = requests.get(wwr_url, headers=headers)
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
