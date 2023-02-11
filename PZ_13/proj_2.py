# В матрице найти сумму элементов второй половины матрицы

import random

# создаём матрицу размером n*n
size = int(input("Enter size matrix: "))
matrix = [[random.randint(0, 10) for r in range(size)] for c in range(size)]

# выводим матрицу
print("<---------------matrix--------------->")
for rows in matrix:
  print(rows)

# ищем сумму элементов второй половины матрицы
list_value_vertical = []
list_value_horizontal = []

for r in range(size):
  for c in range(size):
    if size // 2 <= c:
      list_value_vertical.append(matrix[r][c])
    if size // 2 <= r:
      list_value_horizontal.append(matrix[r][c])

# выводим значения
print(f"list_value_vertical: {list_value_vertical}")
print(f"list_value_horizontal: {list_value_horizontal}")
print(f"sum value_vertical: {sum(list_value_vertical)}")
print(f"sum value_horizontal: {sum(list_value_horizontal)}")