# Дан список A размера N и целое число K. Осуществить
# циклический сдвиг элементов списка вправо на K позиций (при этом A 1 перейдет в
# AK+1, A2 — в AK+2, ..., AN — в A K ). Допускается использовать вспомогательный
# список из 4 элементов.

# -> 7
# -> 1 2 3 4 5 6 7
# <- 5 6 7 1 2 3 4


import random

#функция для сдвига
def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())


# создание списка и его заполнение
N = int(input("Enter size: "))
A = list()

for i in range(N):
  A.append(random.randrange(1, N))

K = int(input("Enter K: "))

# работа функции
print("before:", *A)
shift(A, K)
print("After: ", *A)