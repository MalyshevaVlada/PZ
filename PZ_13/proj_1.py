# В матрице найти суммы элементов каждой строки и поместить их в новый массив.
# Выполнить замену элементов третьего столбца исходной матрицы на полученные суммы.
import random

# создаём двумерный массив (матрица)
count_colums = int(input("Enter count colums: "))
count_rows = int(input("Enter count rows: "))

matrix = [[random.randint(-10, 10) for r in range(count_rows)] for c in range(count_colums)]

# выводим матрицу
print("<---------------matrix--------------->")
print(*[matrix[c] for c in range(count_colums)])
