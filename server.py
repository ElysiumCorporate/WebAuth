# Imports
import sanic
import hashlib
import pymongo

from sanic import Sanic
from sanic.response import json
from hashlib import sha256
from pymongo import MongoClient

# Variables
app = Sanic("ElysiumWeb")
client = MongoClient("YOUR_URL")
db = client.db.elysiumdb
users = db.users

# API Routes
# User authentication
@app.post("/api/login/<username>/<password>")
async def login(request, username, password):
    hashedPassword = sha256(str(password).encode("utf-8")).hexdigest()
    results = users.find_one({"username": username, "password": hashedPassword})
    if results is None:
        return json({"status": "error", "extra": "Invalid login credentials"})
    else:
        return json({"status": "success"})
    
@app.post("/api/register/<username>/<password>")
async def register(request, username, password):
    hashedPassword = sha256(str(password).encode("utf-8")).hexdigest()
    usernameCheck = users.find_one({"username": username})
    # Check if a username already exists
    if usernameCheck is not None:
        return json({"status": "error", "extra": "Username already exists."})
    else:
        users.insert_one({"username": username, "password": hashedPassword})
        return json({"status": "success"})

# E-Mail verification
# Boost the Discord server to unlock this code!
# https://discord.gg/Jme8SD9gBB

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1337)