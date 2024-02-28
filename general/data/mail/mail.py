from Crypto.PublicKey import RSA
import base64

fichier_key = "privacy_enhanced_mail.pem"

with open(fichier_key, 'r') as fichier:
    pem_data = fichier.read()

pem_data = pem_data.replace("-----BEGIN RSA PRIVATE KEY-----", "")
pem_data = pem_data.replace("-----END RSA PRIVATE KEY-----", "")

pem_data = ''.join(pem_data.split())

der_data = base64.b64decode(pem_data)
print(der_data)

# Charger la clé privée RSA à partir de DER-encoded data
cle_privee = RSA.import_key(der_data)
print(cle_privee)

d = cle_privee.d
print(d)