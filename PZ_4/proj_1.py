# Дано вещественное число A и целое число N (N>0). Используя один цикл,
# найти значение выражения 1 - А + А^2 + A^3 + ... + (-1)^N. Условный оператор не использовать.

# -> 5.0 4
# <- 147.0

count = 0   # значение выражения
i = 1      # счётчик
A = input("Enter A: ")
N = input("Enter N: ")


# обработка исключений
while type(A) != float:
  try:
    A = float(A)
  except ValueError:
    A = input("Enter A: ")

while type(N) != int:
  try:
    N = int(N) if int(N) > 0 else int(input("Enter N (N > 0): "))
  except ValueError:
    N = input("Enter N: ")

count = 1 - A

while N - 1 > i:
  i += 1
  count = count + A**i

count = count + (-1)**N

print("expression value: ", count)