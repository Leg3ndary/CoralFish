"""
this isn't illegal btw
"""

import asyncio
import pymongo
import json

"""
IP SCHEMA:

{
    "_id": ip: str,
    "users": {
        user_id(str): tries(int)
    },
    "success": 0,
    "fail": 0
}

"""

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
            f"mongodb+srv://{config.get('MONGO_USER')}:{config.get('MONGO_PASS')}@fishc1.7cztx.mongodb.net/DATA?retryWrites=true&w=majority"
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
        result = self.loop.run_in_executor(None, self.IPS.find_one(query))

        if not result:
            s, f = 1, 0

            if not success:
                s, f = f, s

            new_doc = {
                "_id": ip,
                "users": {
                    str(user_id): 1,
                },
                "success": s,
                "fail": f
            }

            self.loop.run_in_executor(None, self.IPS.insert_one(new_doc))
            print(f"[ NEW ] New IP Requested - {ip} -")
        else:
            if not result.get("users").get(user_id):
                new_user = (user_id, 1)
            else:
                new_user = (user_id, result.get("users").get(user_id) + 1)

            new_users = result.get("users").update(new_user)

            if success:
                s, f = result.get("success") + 1, result.get("fail")
            else:
                s, f = result.get("success"), result.get("fail") + 1
            up_doc = {
                "_id": result.get("_id"),
                "users": new_users,
                "success": s,
                "fail": f
            }

            self.loop.run_in_executor(None, self.IPS.update_one(up_doc))
            

        