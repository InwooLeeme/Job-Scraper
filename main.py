from wwr import extract_wwr
from remoteok import extract_remoteok
from stackover import extract_stackover
from flask import Flask, render_template, redirect

app = Flask("JobScrper")

wwr_result = extract_wwr()

remoteok_result = extract_remoteok()

stackover_result = extract_stackover()

jobs = wwr_result + remoteok_result + stackover_result

# print(jobs)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/detail")
def detail():
    return render_template("detail.html", jobs=jobs)


app.run(host="localhost")
