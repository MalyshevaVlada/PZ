# Из исходного текстового файла (price.txt) выбрать все цены. Посчитать количество
# полученных элементов.


import re

# считываем данные из файла
with open("./price.txt", "r", encoding="utf8") as File:
  text_file = File.read()

# составляем регулярку для поиска цен
p = re.compile(r"\d+[\s]?руб\.\s\d\d\s?коп\.(\s)?", re.X)
list_price = p.finditer(text_file)

# находим количесво цен в тексте
count_price = 1
for i in list_price:
  count_price += 1

print(f"Количество полученных цен: {count_price}")