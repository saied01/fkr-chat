import random
import logging
from datetime import datetime
from typing import Dict

from flask import Flask, render_template, request, session, redirect
from flask_socketio import SocketIO, join_room, leave_room, send
from werkzeug.middleware.proxy_fix import ProxyFix
from string import ascii_uppercase

from config import Config

# Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(fkrchat)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)




# Flask initializer
app = Flask(__name__)

app.config.from_object(Config)

socketio = SocketIO(app)

@app.route("/")
def index():
    return {"msg": "Flask server rinning"}


if __name__ == "__main__":
    socketio.run(app, debug=app.config["DEBUG"])