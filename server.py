from flask import Flask, request
app = Flask(__name__)

import datetime

global odistance
global change

odistance = None
change = 25

@app.route('/api/create', methods=["POST"])
def create():
    time = request.args.get("time")
    timestamp = request.args.get("timestamp")
    distance = request.args.get("distance")

    f = open(f"./logs/{time}_create.txt", "a")
    f.write(f"[{timestamp}] {distance}\n")
    f.close()

    print(f"[{timestamp}] {distance}\n")
    
    return "True"

@app.route('/api/changed', methods=["POST"])
def changed():
    global odistance
    global change
    global old
    time = request.args.get("time")
    timestamp = request.args.get("timestamp")
    distance = request.args.get("distance")
    rdistance = int(distance.split(".")[0])
    
    f = open(f"./logs/{time}.txt", "a")
    f.write(f"[{timestamp}] {distance}\n")
    f.close()

    if not odistance is None:

        if odistance - change >= rdistance <= odistance + change:

            f = open(f"./logs/{time}_changed.txt", "a")
            f.write(f"[{timestamp}] from: {old} to: {distance}\n")
            f.close()
    
    odistance = rdistance
    old = distance
    return "True"

app.run(host="ip", port=5000)
