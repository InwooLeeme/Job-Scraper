import requests
from bs4 import BeautifulSoup

stackover_url = "https://stackoverflow.com/jobs?r=true&q=python"


def extract_stack():
    jobs = []
    r = requests.get(stackover_url)
    html = BeautifulSoup(r.text, "html.parser")


extract_stack()
