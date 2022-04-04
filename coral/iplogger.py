"""
this isn't illegal btw
"""

import asyncio
import pymongo
import json

with open("coral/config.json", "r") as f:
    config = json.load(f)

class IPLogger:
    """
    IPLogger
    """

    def __init__(self, loop) -> None:
        """
        Init
        """
        self.loop = loop
        self.mongo = pymongo.MongoClient(
            f"mongodb+srv://{config.get('MONGOUSER')}:{config.get('MONGOPASS')}@fishc1.7cztx.mongodb.net/DATA?retryWrites=true&w=majority"
        )
        self.DATA = self.mongo["DATA"]
        self.IPS = self.DATA["IPS"]
    
    def log_ip(self, ip: str, user_id: str) -> None:
        """
        Log an ip to check back too later
        """
        query = {
            "_id": ip
        }
        result = self.IPS.find_one(query)

        if not result:
            print(f"[ NEW ] New IP Requested - {ip} -")
        else:
            pass

        