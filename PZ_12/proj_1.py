# В последовательности на n целых чисел умножить все элементы на первый элемент

# -> Enter size list: 3
# <- before: [3, 1, 2]
# <- after: [9, 3, 6]


import random
size = int(input("Enter size list: "))

List_start = [random.randint(-size, size) for value in range(size)]
print(f"before: {List_start}")

List_finish = list(map(lambda value: List_start[0]*value, List_start))
print(f"after: {List_finish}")