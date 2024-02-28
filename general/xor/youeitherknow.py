from pwn import xor

a = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
b = b'myXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkey'
d = []

for c, m in zip(a, b):
    res = xor(bytes([c]), bytes([m]))  # XOR individual bytes
    d.append(chr(res[0]))  # Extract the result as a byte and convert to a character
    result = ''.join(d)

print(result)