import random
import logging
from datetime import datetime
from typing import Dict

from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO, join_room, leave_room, send
from werkzeug.middleware.proxy_fix import ProxyFix
from string import ascii_uppercase

from config import Config

# Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


rooms = {}


# Flask initializer
app = Flask(__name__)

app.config.from_object(Config)

socketio = SocketIO(app)


def generate_unique_code(length):
    while True:
        code = ""
        for _ in range(length):
            code += random.choice(ascii_uppercase)
        
        if code not in rooms:
            break

    return code

# Home root
@app.route("/", methods=["POST", "GET"])
def index():
    session.clear()

    if request.method == "POST":
        # .get devuelve el valor asociado con name, si no hay no devuelve nada
        name = request.form.get("name")
        code = request.form.get("code")
        # .get devuelve el valor asociado con join, pero si no hay devuelve False
        # Como son botones no tienen valor, entonces la idea es que devuelva False SOLO si no se presiono
        join = request.form.get("join", False)
        create = request.form.get("create", False)

        if not name:
            return render_template("home.html", error="Please enter a name.", code=code, name=name)
        
        if join != False and not code:
            return render_template("home.html", error="Please enter a room code.", code=code, name=name)
        
        room = code
        if create != False:
            room = generate_unique_code(4)
            rooms[room] = {"members": 0, "messages": []}
        elif code not in rooms:
            return render_template("home.html", error="Room does not exist.", code=code, name=name)
    
        session["room"] = room
        session["name"] = name
        return redirect(url_for("room"))
    
    return render_template("home.html")

# Chat root
@app.route("/room")
def room():

    # Para que no puedas ir a '/room' sin tocar el boton de join/create
    room = session.get("room")
    if room is None or session.get("name") is None or if room not in rooms:
        return redirect(url_for("home"))

    return render_template("room.html")

if __name__ == "__main__":
    socketio.run(app, debug=app.config["DEBUG"])