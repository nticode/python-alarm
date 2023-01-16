from flask import Flask, request
app = Flask(__name__)

import datetime
import os

@app.route('/api/create', methods=["POST"])
def create():
    time = request.args.get("time")
    timestamp = request.args.get("timestamp")
    distence = request.args.get("distence")

    f = open(f"./logs/{time}.txt", "a")
    f.write(f"[{timestamp}] {distence}\n")
    f.close()

    print(f"[{timestamp}] {distence}\n")
    
    return "True"

app.run(host='ip', port=5000)
