import requests
from bs4 import BeautifulSoup

stackover_url = "https://stackoverflow.com/jobs?r=true&q=python"


def get_last_page():
    page_list = []
    r = requests.get(stackover_url)
    html = BeautifulSoup(r.text, "html.parser")
    page = html.find("div", class_="s-pagination")
    page_link = page.find_all("a", class_="s-pagination--item")
    for items in page_link[:-1]:
        page_number = items.find("span").get_text()
        page_list.append(page_number)
    return page_list


def extract_jobs(page_list):
    jobs = []
    for pages in page_list:
        url = f"https://stackoverflow.com/jobs?q=python&pg={pages}"
        r = requests.get(url)
        html = BeautifulSoup(r.text, "html.parser")
        table = html.find("div", class_="js-search-results")
        job_table = table.find("div", class_="grid--cell")
        search_result = job_table.find_all("div", class_="-job")
        for each_job in search_result:
            apply_link = each_job.find("a", class_="s-link").get('href')
            title = each_job.find("a", class_="s-link").string
            up_time = each_job.find("ul", class_="mt4").find(
                "li").find("span", class_="")
            company = each_job.find(
                "h3", class_="fc-black-700").find("span").get_text("", strip=True)
            if(up_time is None):
                up_time = None
                continue
            else:
                up_time = up_time.string
            jobs_dict = {
                "title": title,
                "applyLink": f"https://stackoverflow.com/{apply_link}",
                "company": company,
                "upTime": up_time
            }
            jobs.append(jobs_dict)
    return jobs


def extract_stackover():
    page_list = get_last_page()
    result = extract_jobs(page_list)
    return result
