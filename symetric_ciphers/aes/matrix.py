def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    matrix = []
    for i in range(0, len(text), 4):
        matrix.append(list(text[i:i+4]))
    return matrix

# print(bytes2matrix('bonjour'))

def matrix2bytes(matrix):
    text = ''
    for i in matrix:
        for j in i:
            text += chr(j)
    return text     

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

# print(matrix2bytes(matrix))
