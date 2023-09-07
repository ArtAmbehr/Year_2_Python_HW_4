# 1. Напишите функцию для транспонирования матрицы

matrix = [[3, 4, 8], [5, 6, 9], [7, 8, 6]]
matrix_transposition = [list(row) for row in zip(*matrix)]

print(matrix_transposition)
