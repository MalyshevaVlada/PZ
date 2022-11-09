# Задача: Дано трёхзначное число. Найти сумму и произведение его цифр.
# -> 233
# <- sum: 8
# <- product: 18

try:
    number = int(input("Enter three-digit: "))
except ValueError:
    print("you entered not a number")
else:
    if 99 < abs(number) < 1000:
      sum = (int(number / 100)) + (abs(int(number / 10)) % 10) + (abs(number) % 10)
      product = (int(number / 100)) * (abs(int(number / 10)) % 10) * (abs(number) % 10)
      print(f"number: {number}\nsum = {sum}\nproduct = {product}\n")
    else:
      print("you entered not a three-digit number")