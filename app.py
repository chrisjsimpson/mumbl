from flask import Flask, render_template, request
import string
import requests
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

app = Flask(__name__)

AUTH_ID = os.getenv("AUTH_ID")
AUTH_PASSWORD = os.getenv("AUTH_PASSWORD")
SERVER_IP = os.getenv("SERVER_IP")


@app.route("/")
def hello_world():
    return render_template("form.html")


@app.route("/", methods=["POST"])
def host():
    subdomain = request.form.get("text", None)
    if subdomain is not None:
        "".join(ch for ch in string.printable if ch.isalnum())
    subdomain = subdomain.replace(" ", ".")
    requests.post(
        f"https://api.cloudns.net/dns/add-record.json/?auth-id={AUTH_ID}&auth-password={AUTH_PASSWORD}&domain-name=mumbl.app&record-type=A&host={subdomain}&record={SERVER_IP}&ttl=3600"
    )

    return f"Your address is: <a href='http://{subdomain}mumbl.app'>{subdomain}.mumbl.app</a>"
