import requests
from bs4 import BeautifulSoup

remoteok_url = "https://remoteok.io/remote-dev+python-jobs"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


def extract_remoteok():
    r = requests.get(remoteok_url, headers=headers)
    html = BeautifulSoup(r.text, "html.parser")
    table = html.find("table")
    tr = table.find_all("tr", class_="job")
    print(tr)


extract_remoteok()
