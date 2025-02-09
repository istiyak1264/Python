# website: https://cryptohack.org/challenges/aes/
#problem name: Structure of AES

#converting byte value in matrix
def bytes2matrix(text):
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

#converting matrix value in bytes
def matrix2bytes(matrix):
    return bytes(sum(matrix, []))

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

#printing the flag
print(matrix2bytes(matrix).decode())
