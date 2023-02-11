# В матрице найти суммы элементов каждой строки и поместить их в новый массив.
# Выполнить замену элементов третьего столбца исходной матрицы на полученные суммы.

import random

# создаём двумерный массив (матрица)
count_colums = int(input("Enter count colums: "))
count_rows = int(input("Enter count rows: "))

matrix = [[random.randint(-10, 10) for r in range(count_rows)] for c in range(count_colums)]

# выводим матрицу
print("<---------------matrix--------------->")
for rows in matrix:
  print(rows)

# создаём новый массив для суммы строк
sum_rows_matrix = [sum(rows) for rows in matrix]
print("<----------sum_rows_matrix----------->")
print(sum_rows_matrix)

# выполняем замену элементов третьего столбца исходной матрицы на полученные суммы
for r in range(count_rows):
  for c in range(count_colums):
    if matrix[r][c] == matrix[r][count_colums - 1]:
      matrix[r][c] = sum_rows_matrix[r]

# выводим матрицу
print("<---------------new matrix--------------->")
for rows in matrix:
  print(rows)