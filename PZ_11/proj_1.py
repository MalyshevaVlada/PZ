# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:

# Исходные данные:
# Количество чисел:
# Положительные числа:
# Количество положительных чисел:
# Отрицательные числа:
# Количество отрицательных чисел:


# переменные
L = ["-5 -4 -3 -2 -1 0 1 2 3 4 5"]

# функции
def from_file_to_list(str_name_file):
  f = open(str_name_file, "r")
  k = f.read().split()
  for i in range(len(k)):
    k[i] = int(k[i])
  f.close()
  return k

def positive_num(mas):
  mas_positive = []
  for i in range(len(mas)):
    if mas[i] > 0:
      mas_positive.append(mas[i])
  return mas_positive


def negative_num(mas):
  mas_negative = []
  for i in range(len(mas)):
    if mas[i] < 0:
      mas_negative.append(mas[i])
  return mas_negative


# запись списка в файл
file_one = open("text_one.txt", "w")
file_one.writelines(L)
file_one.close()

# формируем новый текстовый фал и выполняем обработку элементов
file_two = open("text_two.txt", "w")
mas = from_file_to_list("text_one.txt")

file_two.writelines(f"Исходные данные: {mas}\n")
file_two.writelines(f"Количество чисел: {len(mas)}\n")
file_two.writelines(f"Положительные числа: {positive_num(mas)}\n")
file_two.writelines(f"Количество положительных чисел: {len(positive_num(mas))}\n")
file_two.writelines(f"Отрицательные числа: {negative_num(mas)}\n")
file_two.writelines(f"Количество отрицательных чисел: {len(negative_num(mas))}")
file_two.close()

file_two = open("text_two.txt", "r")
print(file_two.read())
file_two.close()
