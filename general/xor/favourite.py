a = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
b = []


for i in a:
    b.append(i)

for i in range(256):
    z = []
    for j in a:
        xor = j ^ i
        z.append(xor)

    res = bytes(z).decode('ascii', 'ignore')
    if 'crypto' in res:
        print(res)

    