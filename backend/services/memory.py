from datetime import datetime,timezone
from pymongo import MongoClient
class MemoryStore:
    def __init__(self,uri,db): self.client=MongoClient(uri,serverSelectionTimeoutMS=1500); self.messages=self.client[db].messages
    def health(self):
        try:self.client.admin.command('ping');return True
        except Exception:return False
    def add_message(self,sid,role,content): self.messages.insert_one({'session_id':sid,'role':role,'content':content,'created_at':datetime.now(timezone.utc)})
    def get_messages(self,sid,limit=20):
        cur=self.messages.find({'session_id':sid},{'_id':0}).sort('created_at',1).limit(limit)
        return [{'role':x['role'],'content':x['content'],'created_at':x['created_at'].isoformat()} for x in cur]
