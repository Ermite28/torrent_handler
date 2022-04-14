from app import app, message_broker
from flask import Flask, render_template, url_for, request
from .dummy_data import dummy_data
import json


@app.route("/download", methods=["POST", "GET"])
def download():
    data = request.json
    if message_broker.publish_new_torrent(json.dumps(data)):
        return "Download data in progress..."
    else:
        return "Fail"


@app.route("/")
def index():
    return "Index"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
