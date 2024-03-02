import jwt

#default parameter key is "secret"
default_key = "secret"
encoded = jwt.encode({"username":"admin","admin":True}, key, algorithm="HS256")

print(encoded)