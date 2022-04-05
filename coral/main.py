import asyncio

import json
import pymongo
import random
import time
import flask
from discord.ext import oauth
from emojis import FishE as fishe
from iplogger import IPLogger
# motor and flask async have massive problems working with each other so we just use to_thread

"""
Database Style


DATA:
    USERS:
        USER SCHEMA
    IPS:
        IP SCHEMA

USER SCHEMA:

{
    "_id": user id: str,
    "fish": {
        "Bream": 0,
        "Gudgeon": 0,
        "Carp": 0,
        "Loach": 0,
        "Bass": 0,
        "Piranha": 0,
        "Koi": 0,
        "Rainbow": 0,
        "Shark": 0
    }
}

IP SCHEMA:

{
    "_id": ip: str,
    "users": {
        user_id(str): tries(int)
    },
    "success": 0,
    "fails": 0
}

"""
app = flask.Flask(__name__)
loop = asyncio.get_event_loop()

with open("coral/config.json", "r") as f:
    config = json.load(f)
    print("Loaded Config")

oclient = oauth.OAuth2Client(
    client_id = 929489293725040671,
    client_secret = config.get("CLIENT_SECRET"),
    redirect_uri = "https://discord.com/api/oauth2/authorize?client_id=929489293725040671&redirect_uri=https%3A%2F%2Fgithub.com%2FLeg3ndary%2FCoralFish%2Fblob%2Fmain%2FACCEPTED.md&response_type=code&scope=identify",
    scopes = ["identify"]
)
print("Loaded Oauth2Client")

class FishMongo:
    """
    FishMongo
    """

    def __init__(self) -> None:
        """
        Init
        """
        self.run = True
        self.mongo = pymongo.MongoClient(
            f"mongodb+srv://{config.get('MONGO_USER')}:{config.get('MONGO_PASS')}@fishc1.7cztx.mongodb.net/DATA?retryWrites=true&w=majority"
        )
        self.DATA = self.mongo["DATA"]
        self.USERS = self.DATA["USERS"]
        print("Loaded MongoDB")

mongo = FishMongo()
iplogger = IPLogger()

def match_code(code: str, user: int, discrim: int):
    """
    Verify a code
    """
    cor = int(time.time()) * int(user) + int(discrim)

    if int(code) == cor:
        pass
    else:
        pass


@app.route("/")
async def home():
    """
    Simple Home Page
    """
    api_status = {"API_STATUS": 200}
    return api_status

@app.route("/fish/<int:unix>/<int:user_id>")
async def fish(unix, user_id):
    """
    Fish for some fishies
    """
    chance = random.randint(0, 1000)
    if chance < 1:
        # 5 Star
        pass
    elif chance < 11:
        # 4 star
        pass
    elif chance < 100:
        # 3 Star
        pass
    elif chance < 350:
        # 2 star
        pass
    else:
        # 1 star
        pass

app.run(
    host="0.0.0.0", 
    port=8080
)