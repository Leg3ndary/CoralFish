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

    def __init__(self) -> None:
        """
        Init
        """
        self.mongo = pymongo.MongoClient(
            f"mongodb+srv://{config.get('MONGOUSER')}:{config.get('MONGOPASS')}@fishc1.7cztx.mongodb.net/DATA?retryWrites=true&w=majority"
        )
        self.DATA = self.mongo["DATA"]
        self.IPS = self.DATA["IPS"]
    
    def log_ip(self, ip: str, user_id: str, success: bool) -> None:
        """
        Log an ip to check back too later
        """
        query = {
            "_id": ip
        }
        result = self.IPS.find_one(query)

        if not result:
            values = (1, 0)

            if not success:
                values = (0, 1)

            new_doc = {
                "_id": ip,
                "users": {
                    str(user_id): 1,
                },
                "success": values[0],
                "fails": values[1]
            }
            asyncio.to_thread(self.IPS.insert_one(), new_doc)
            print(f"[ NEW ] New IP Requested - {ip} -")
        else:
            pass


        