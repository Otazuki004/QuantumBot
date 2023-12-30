from root import DATABASE
from root.helper.telegraph import telegraph 

db = DATABASE["MAIN"]

async def add_profile_to_users(message, user_id: int, profile):
     filter = {"user_id": user_id}
     if await telegraph(message, profile) == False:
         return           
     else:
         link = await telegraph(message, profile)
         update = {"$set": {"profile": link}}
         db.update_one(filter, update)
     

async def get_profile_from_users(user_id: int):
      string = {"user_id": user_id}
      mm = db.find_one(string)
      try:
         return mm["profile"]
      except KeyError:
          return "https://telegra.ph/file/d04fc83f3658be1349175.jpg"
          
