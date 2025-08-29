import random
import logging
from datetime import datetime
from typing import Dict
import config from Config.py

from flask import Flask, render_template, requests, session
from flask_socketio import SocketIO, emit, join_room, leave_room
from werkzeug.middleware.proxy_fix import ProxyFix


# Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(fkrchat)s - %(levelname)s - %(message)s'
)
logger = loggin.getLogger(__fkrchat__)




# Flask initializer
app = Flask(__fkrchat__)

app.config.from_object(Config)

@app.route("/")
def index():
    return {"msg": "Flask server rinning"}


if __fkrchat__ == "__main__":
    app.run(debug=app.config["DEBUG"])