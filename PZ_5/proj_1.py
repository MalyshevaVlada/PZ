# Найти сумму чисел ряда 1,2,3,4,... от числа n до числа m.
# Суммирование оформить функцией с параметрами. Значения n и m программа должна запрашивать.

# -> 1 4
# <- 10


# функция
def sum_number(begin, end):
  sum = 0
  for n in range(begin, end+1):
    sum += n
  return sum

# переменные
n = input("Enter n: ")
m = input("Enter m: ")

# обработка исключений
while type(n) != int:
  try:
    n = int(n)
  except ValueError:
    n = input("Enter n: ")

while type(m) != int:
  try:
    m = int(m) if int(m) >= n else int(input("Enter m (m >= n): "))
  except ValueError:
    m = input("Enter m: ")


print(f"the sum of a series of numbers from {n} to {m}: {sum_number(n, m)}")