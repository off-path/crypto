from Crypto.PublicKey import RSA
import base64

fichier_rsa_pub = "bruce_rsa.pub"

with open(fichier_rsa_pub, 'rb') as fichier:
    fichier = fichier.read()

print(fichier)
certif = RSA.import_key(fichier)

moduel_rsa = certif.n
print(moduel_rsa)