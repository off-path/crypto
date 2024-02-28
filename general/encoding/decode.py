import base64

ASCII = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
ASCII = [chr(i) for i in ASCII]
print(''.join(ASCII))

hex = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
print(bytes.fromhex(hex))

b64 = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
b64 = bytes.fromhex(b64)
print(base64.b64encode(b64))

bbint = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
print(bbint.to_bytes((bbint.bit_length() + 7) // 8, 'big').decode())

