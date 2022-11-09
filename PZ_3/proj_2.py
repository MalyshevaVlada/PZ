# Даны три целых числа, одно из которых отлично от двух других, равных между собой.
# Определить порядковый номер числа, отличного от остальных

# -> 6 6 4
# <- 3

# примечание: в этом решение индексация (порядковый номер) начинается с 1 (единицы)

# переменные
a = input("Enter one number: ")
b = input("Enter two number: ")
c = input("Enter three number: ")

# обработка исключений
while type(a) != int:
  try:
    a = int(a)
  except ValueError:
    a = input("Enter one number: ")

while type(b) != int:
  try:
   b = int(b)
  except ValueError:
    b = input("Enter two number: ")

while type(c) != int:
  try:
    c = int(c)
  except ValueError:
    c = input("Enter three number: ")


# проверка на истинность условия и вывод результата
print("(´｡•ㅅ•｡`)")

if a == b == c:
  print("All three numbers are the same")
elif a == b and c != a:
    print("index number: 3")
elif a == c and b != a:
    print("index number: 2")
elif b == c and a != c:
    print("index number: 1")
elif a != b != c:
    print("All three numbers are different")
else:
   print("We've reached what we shouldn't have")