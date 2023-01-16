import json
from flask import Flask, request
app = Flask(__name__)


@app.route('/api/create', methods=["POST"])
def create():
    time = request.args.get("time")
    dictence = request.args.get("dictence")
    print("recived")
    
    return json.dumps({'name': 'alice',
                       'email': 'alice@outlook.com'})

app.run(host='192.168.0.9', port=5000)
