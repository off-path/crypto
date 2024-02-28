a = 13
b = 'label'
c = []

for i in b:
    xor = a ^ ord(i)
    c.append(chr(xor))

result = ''.join(c)
print(result)
