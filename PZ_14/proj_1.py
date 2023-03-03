# Из исходного текстового файла (price.txt) выбрать все цены. Посчитать количество
# полученных элементов.

import re

with open("price.txt", "r") as File:
  text_file = File.read()

p = re.compile(r"\d+[\s]?руб\.\s\d\d\s?коп\.(\s)?", re.X)
list_price = p.finditer(text_file)

count_price = 1

for i in list_price:
  count_price += 1

print(count_price)