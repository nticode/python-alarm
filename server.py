from flask import Flask, request
app = Flask(__name__)

import datetime
import os

@app.route('/api/create', methods=["POST"])
def create():
    time = request.args.get("time")
    timestamp = request.args.get("timestamp")
    distance = request.args.get("distance")

    f = open(f"./logs/{time}.txt", "a")
    f.write(f"[{timestamp}] {distance}\n")
    f.close()

    print(f"[{timestamp}] {distance}\n")
    
    return "True"

app.run(host='192.168.0.9', port=5000)
