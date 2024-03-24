from flask import Flask,request
import json


app = Flask(__name__)

@app.get("/")
def home():
    data = json.loads(request.args.get("text"))
    print(json.dumps(data,indent=4))
    return "HI"


app.run()