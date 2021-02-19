from wwr import extract_wwr
from remoteok import extract_remoteok
from stackover import extract_stackover
from flask import Flask, render_template, redirect

app = Flask("JobScrper")

wwr_result = extract_wwr()

remoteok_result = extract_remoteok()

stackover_result = extract_stackover()


@app.route("/")
def home():
    return render_template("index.html")


app.run(host="localhost")
