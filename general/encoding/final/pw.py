from pwn import * # pip install pwntools
import codecs
import base64
import json

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    print("print here", json.loads(line.decode()))
    return json.loads(line.decode())

def json_send(hsh):
    if isinstance(hsh, bytes):
        hsh = hsh.decode('utf-8')
    request = json.dumps(hsh).encode()
    r.sendline(request)

while True:
    print("there")
    received = json_recv()

    print(received["type"])

    if received["type"] == "rot13":
        to_send = {
            "decoded":codecs.decode(received["encoded"], 'rot_13')
        }
        print('decoded: ', to_send)

    elif received["type"] == "utf-8":
        res = ''.join([chr(i) for i in received["encoded"]])
        to_send = {
            "decoded": res
        }
        print('decoded: ', to_send)

    elif received["type"] == "base64": 
        to_send = {
            "decoded":base64.b64decode(received["encoded"]).decode('utf-8')
        }
        print('decoded: ', to_send)

    elif received["type"] == "hex": 
        to_send = {
            "decoded": bytes.fromhex(received["encoded"]).decode('utf-8')
        }
        print('decoded: ', to_send)

    elif received["type"] == "bigint":
        decoded_bytes = int(received["encoded"], 0).to_bytes((int(received["encoded"], 0).bit_length() + 7) // 8, 'big')
        to_send = {
            "decoded": decoded_bytes.decode('utf-8')
        }
    else: 
        to_send = {
            "decoded": "changeme"
        }
    json_send(to_send)

    if r.can_recv():
        json_recv()
