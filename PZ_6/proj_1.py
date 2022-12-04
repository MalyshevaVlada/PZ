# Дан список A размера N. Вывести его элементы в следующем порядке: A1, AN,
# A2 , AN-1, A3, AN-2 ...

# -> 4 7 4 3 9 7 5 2 4 6
# <- 4 6 7 4 4 2 3 5 9 7 

import random

size = int(input("Enter size: "))
A = list()

for i in range(size):
  A.append(random.randrange(1, size))

print(*A)

for i in range(size // 2):
  print(A[i], A[size - i - 1], end=' ')
if size % 2 != 0:
    print(A[size // 2])