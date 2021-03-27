import numpy as np
import os


def is_magic(matrix):
    if np.array_equal(np.unique(matrix.sum(axis=1)), np.unique(matrix.sum(axis=0))):
        return True
    else:
        return False


def generate_magic(n):
    generated_matrix = np.zeros([n, n])
    for i in range(n):
        generated_matrix[i][i] = (n - 1) / 2
        for k in range(n):
            if k < (n - 1) / 2:
                if i + k + 1 < n:
                    generated_matrix[i][i + k + 1] = k
                else:
                    generated_matrix[i][i + k + 1 - n] = k
            else:
                if k == (n - 1) / 2:
                    pass
                else:
                    if k + i < n:
                        generated_matrix[i][i + k] = k
                    else:
                        generated_matrix[i][i + k - n] = k

    result_square = np.zeros([n, n])
    for i in range(n):
        for k in range(n):
            result_square[i][k] = generated_matrix[i][k] * n + generated_matrix[i][n - 1 - k] + 1

    return result_square


def find_in_matrix(value, input_matrix):
    size = len(input_matrix)
    for i in range(size):
        for j in range(size):
            if input_matrix[i][j] == value:
                return [i, j]

    return [-1, -1]


def string_to_magic_square(string, magic_square):
    n = len(magic_square)
    string = string + " " * (n * n - len(string))
    res = [[" " for x in range(n)] for y in range(n)]
    for i in range(len(string)):
        i_pos, j_pos = find_in_matrix(i + 1, magic_square)
        res[i_pos][j_pos] = string[i]
    return res


def magic_square_to_string(crypt_square, magic_square):
    string = ""
    for i in range(len(crypt_square)**2):
        i_pos, j_pos = find_in_matrix(i + 1, crypt_square)
        string += magic_square[i_pos][j_pos]
    return string


print("Hello, " + os.environ.get("USERNAME") + "!\nEnter your string:")
input_string = str(input())
size_of_matrix = int(np.ceil(np.sqrt(len(input_string))))
magic = generate_magic(size_of_matrix)
print(magic)
matrix = string_to_magic_square(input_string, magic)
print(matrix)
string = magic_square_to_string(magic, matrix)
print(string)
