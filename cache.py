import time
from pymemcache.client import base
client = base.Client(('localhost', 11211))

client.set('country:France', 'Paris')
print("Country namespace - France:", client.get('country:France'))



client.set('user:session:user_id', '123456856', expire=5)
print("\nUser session - Read user_id immediately:", client.get('user:session:user_id'))
print("Sleeping for 5 seconds...")
time.sleep(5)
print("User session - Read user_id after 5 seconds:", client.get('user:session:user_id'))




client.set("site:visits", 0)
print("\nSite namespace - Initial visits count:", client.get("site:visits"))

client.incr("site:visits", 1)
client.decr("site:visits", 1)
client.incr("site:visits", 1)
client.incr("site:visits", 1)

print("Site namespace - Visits count after increments:", client.get("site:visits"))



client.add("app:all_names", "Ahmad")
client.append("app:all_names", "Ali")
print("\nApp namespace - All names after appending 'Ali':", client.get("app:all_names"))
client.append("app:all_names", "Hassan")
client.append("app:all_names", "Mohammed")
print("App namespace - All names after appending 'Hassan' and 'Mohammed':", client.get("app:all_names"))






client.flush_all()
print("\nApp namespace - All names after flush_all:", client.get("app:all_names"))  




client.set("user:profile:name", "Ahmad")
client.set("user:profile:gender", "male")
print("\nUser profile namespace - Name:", client.get("user:profile:name"))
print("User profile namespace - Gender:", client.get("user:profile:gender"))
client.delete("user:profile:name")
print("User profile namespace - Name after deletion:", client.get("user:profile:name")) 
print("User profile namespace - Gender remains:", client.get("user:profile:gender"))



user_data = {
    "user:data:name": "Ahmad",
    "user:data:age": 24, 
    "user:data:gender": "male",
    "user:data:no_of_visits": 10,
    "user:data:food": "Biryani"
}



client.set_multi(user_data)
print("\nUser data namespace - Name:", client.get("user:data:name"))
print("User data namespace - Age:", client.get("user:data:age"))
print("User data namespace - Gender:", client.get("user:data:gender"))
print("User data namespace - No of visits:", client.get("user:data:no_of_visits"))
print("User data namespace - Food:", client.get("user:data:food"))
