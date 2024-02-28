import requests
from datetime import datetime, timedelta
import json

def get_ciphertext():
    url = "http://aes.cryptohack.org/flipping_cookie/get_cookie/"
    r = requests.get(url)
    cookie = (json.loads(r.text))['cookie']
    return cookie

def decrypt_ccb(cookie, iv):
    url = "http://aes.cryptohack.org/flipping_cookie/check_admin/"+cookie+'/'+iv
    r = requests.get(url)
    # Extraire le texte brut de la réponse HTTP
    flag = r.text.strip()
    return flag


def flip(cookie, plain):
    # var to find th admin=false in the cookie
    start = plain.find(b'admin=False')
    cookie = bytes.fromhex(cookie)
    # Récupérer le IV original du cookie
    iv = [0xff]*16
    # Initialiser une liste pour stocker le cookie chiffré modifié
    cipher_fake = list(cookie)
    # Texte clair souhaité à injecter dans le cookie chiffré
    fake = b';admin=True;'
    # Pour chaque octet dans le texte clair souhaité
    for i in range(len(fake)):
       # Calculer le nouveau octet du cookie chiffré en XORant avec le texte clair souhaité et le texte chiffré original
       cipher_fake[16+i] = plain[16+i] ^ cookie[16+i] ^ fake[i]
       iv[start+i] = plain[start+i] ^ cookie[start+i] ^ fake[i]

    # Convertir le cookie chiffré modifié et l'IV en hexadécimal
    cipher_fake = bytes(cipher_fake).hex()
    iv = bytes(iv).hex()
    return cipher_fake, iv

expires_at = (datetime.today() + timedelta(days=1)).strftime("%s")
plain = f"admin=False;expiry={expires_at}".encode()
cookie = get_ciphertext()
cookie, iv = flip(cookie, plain)
print(decrypt_ccb(cookie, iv))
