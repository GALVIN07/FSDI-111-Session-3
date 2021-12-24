from flask import Flask
from datetime import datetime

app = Flask(__name__)
VERSION = "1.0.0"

@app.get("/version")
def get_version():
    out = {}
    out["server_time"] = (
        datetime.now().strftime("%F %H:%M:%S"))
    out["version"] = VERSION
    return out

