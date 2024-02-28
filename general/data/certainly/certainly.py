from Crypto.PublicKey import RSA
import base64

fichier_der = "privatecert.der"

with open(fichier_der, 'rb') as fichier:
    certificat_der_data = fichier.read()
print(certificat_der_data)

certif = RSA.import_key(certificat_der_data)
print(certif)

module_rsa = certif.n
print(module_rsa)