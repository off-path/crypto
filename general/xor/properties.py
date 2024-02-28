key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
result_xor1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
result_xor2 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

#on fou tout en bytes
key1 = bytes.fromhex(key1)
result_xor1 = bytes.fromhex(result_xor1)
result_xor2 = bytes.fromhex(result_xor2)
flag = bytes.fromhex(flag)

#zip pour associé les bytes correspondant, puis boucle pour xor les bytes entre eux
key2 = bytes(x ^ y for x, y in zip(key1, result_xor1))
key3 = bytes(x ^ y for x, y in zip(key2, result_xor2))

#same, mais *4
flag = bytes(w ^ x ^y ^ z for w, x, y, z in zip(flag, key1, key3, key2))

print(flag)