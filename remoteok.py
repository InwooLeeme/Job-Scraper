import requests
from bs4 import BeautifulSoup

remoteok_url = "https://remoteok.io/remote-dev+python-jobs"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


def extract_remoteok():
    remoteok_jobs = []
    r = requests.get(remoteok_url, headers=headers)
    html = BeautifulSoup(r.text, "html.parser")
    table = html.find("table")
    tr = table.find_all("tr", class_="job")
    for items in tr:
        location = items.find("div", class_="location")
        company = items.find("h3", {"itemprop": "name"})
        apply_link = items.find("a", class_="companyLink")
        title = items.find("a", class_="companyLink").find("h3")
        up_time = items.find("time")
        if(location):
            location = location.string
        else:
            location = "None"
        remote_dict = {
            "title": title.string,
            "company": company.string,
            "location": location,
            "apply_link": f"https://remoteok.io{apply_link.get('href')}",
            "upTime": up_time.string
        }
        remoteok_jobs.append(remote_dict)
    return remoteok_jobs
