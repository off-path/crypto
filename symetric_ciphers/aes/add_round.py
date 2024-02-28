from matrix import matrix2bytes 

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(state, round_key):
    result = []
    #position on line
    for i in range(4):
        row = []
        #position on column
        for j in range(4):
            #xor postion, add it on row table
            row.append(state[i][j] ^ round_key[i][j])
        #add line on row table
        result.append(row)
    res = matrix2bytes(result)
    return res



# print(add_round_key(state, round_key))
