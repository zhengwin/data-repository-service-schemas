import pymongo

class Model:
    def __init__(self):
      self.client = pymongo.MongoClient("mongodb://localhost:27017/")
      self.db = self.client["drs_stores"]
      self.objects = self.db["objects"]

    def create(self, dict):
      return self.objects.insert_one(dict)

    def getObject(self, object_id):
      return self.objects.find_one({"id": object_id})

    def getAllObjects(self):
        print(list(self.objects.find()))
