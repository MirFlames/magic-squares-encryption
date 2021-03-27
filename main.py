import numpy as np  # Для работы с матрицами
import os  # Для приветствия пользователя


def generate_magic(n):
    """ Функция генерации магического квадрата размерностью n на n """
    if n % 2 == 0:
        n += 1

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
    """ Функция поиска в какой строке и столбце расположен элемент в матрице """
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
print("Length of text: " + str(len(input_string)) + " symbols\n")

size_of_matrix = int(np.ceil(np.sqrt(len(input_string))))  # Расчет размеров магического квадрата
magic = generate_magic(size_of_matrix)  # Генерация магического квадрата полученной выше размерности
print("Magic square:\n", magic)  # Вывод магического квадрата на экран
matrix = string_to_magic_square(input_string, magic)  # Шифрование строки
print("Encrypted string in matrix:\n", matrix)  # Вывод зашифрованной строки, имеющей теперь вид двумерного массива
string = magic_square_to_string(magic, matrix)  # Обратное преобразование в строку
print("Decrypted string:\n", string)  # Вывод исходной строки
