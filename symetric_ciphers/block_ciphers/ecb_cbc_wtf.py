import requests
import json
from pwn import xor

def get_ciphertext():
    url = "http://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/"
    r = requests.get(url)
    ct = (json.loads(r.text))['ciphertext']
    return ct

def decrypt_ecb(ct):
    url = "http://aes.cryptohack.org/ecbcbcwtf/decrypt/"+ct
    r = requests.get(url)
    # Extraire le texte en clair de la réponse JSON
    pt = (json.loads(r.text))['plaintext']
    return pt

c = get_ciphertext()
# get iv
iv = bytes.fromhex(c[:32])
# split in 2 parts for decrypt in ECB
ct = [c[32:64], c[64:]]

# decrypt the 2 partq
pt_ecb = [bytes.fromhex(decrypt_ecb(i)) for i in ct]
pt = []

# xor between iv and the first part
pt.append(xor(iv, pt_ecb[0]).decode())
print('first part of the flag', pt)
# xor between iv and the second part
pt.append(xor(bytes.fromhex(ct[0]), pt_ecb[1]).decode())
print('first part of the flag', pt)

# Afficher le texte en clair complet
print(''.join(pt))
