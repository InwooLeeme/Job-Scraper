import requests
from bs4 import BeautifulSoup

stackover_url = "https://stackoverflow.com/jobs?r=true&q=python"


def extract_stack():
    jobs = []
    r = requests.get(stackover_url)
    html = BeautifulSoup(r.text, "html.parser")
    table = html.find("div", class_="js-search-results")
    job_table = table.find("div", class_="grid--cell")
    search_result = job_table.find_all("div", class_="-job")
    for each_job in search_result:
        apply_link = each_job.find("a", class_="s-link")
        print(apply_link)


extract_stack()
