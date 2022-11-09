# Задача: Даны три целых числа: A, B, C.
# Проверить истинность высказывания: «Ровно два из чисел A, B, C являются положительными»
# -> 1 5 -10
# <- true

# примечание: в этом решении 0 (ноль) воспринимается как отрицательное число


# переменные
count = 0
a = input("Enter one number: ")
b = input("Enter two number: ")
c = input("Enter three number: ")

# обработка исключений
while type(a) != int:
  try:
    a = int(a)
    if a > 0: count += 1
  except ValueError:
    a = input("Enter one number: ")

while type(b) != int:
  try:
   b = int(b)
   if b > 0: count += 1
  except ValueError:
    b = input("Enter two number: ")

while type(c) != int:
  try:
    c = int(c)
    if c > 0: count += 1
  except ValueError:
    c = input("Enter three number: ")


# проверка на истинность условия и вывод результата
if count == 3:
  print("(∿°○°)∿ ︵ false")
  print("Exactly three out of three numbers are positive")

elif count == 2:
  print("(∿°○°)∿ ︵ true")
  print("Exactly two out of three numbers are positive")

elif count == 1:
  print("(∿°○°)∿ ︵ false")
  print("Exactly one out of three numbers are positive")

elif count == 0:
  print("(∿°○°)∿ ︵ false")
  print("None of the three numbers is positive")
else:
  print("We've reached what we shouldn't have")