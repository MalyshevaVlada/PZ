# дан целочисленный список размера N, содержащий ровно два одинаковых элемента.
# Найти номера одинаковых элементов и вывести эти номера в порядке возрастания

# -> 6
# -> [1, 2, 3, 4, 5, 2]
# <- 1 5

size = int(input("Enter size: "))
List = list()

for i in range(size):
  List.append(int(input(f"Enter N[{i}] = ")))

for i in range(size):
  for j in range(i):
    if List[i] == List[j]:
      print(f"List[{j}] = {List[j]}")
      print(f"List[{i}] = {List[i]}")
      break
print("Bye!")