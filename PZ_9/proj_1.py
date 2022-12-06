# Сгенерировать словарь вида {0: 1, 1:1, 2:4, 3:9, 4:16, 5:25, 6:36}
# удалив из него второй и третий элементы. отобразить исходный и получившийся словарь.
# использовать for, range.

# -> 7
# <- {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# <- {0: 0, 1: 1, 4: 16, 5: 25}

DICT = {}
size = input("Enter size dict: ")

# обработка исключений
while type(size) != int:
    try:
        size = int(size)
    except ValueError:
        size = input("Enter size dict: ")

# инициализация словаря
for i in range(size):
    DICT[i] = i * i

# вывод словаря
print(f"before: {DICT}")

# удаление элементов
LIST = list(map(int, input("what elements do you want to remove? ").split()))

for i in range(len(LIST)):
    if LIST[i] in DICT:
        del DICT[LIST[i]]

# вывод словаря
print(f"After: {DICT}")