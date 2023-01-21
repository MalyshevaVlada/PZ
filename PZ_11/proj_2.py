# Из предложенного текстового файла (text18-16.txt) вывести на экран его содержимое,
# количество букв в верхнем регистре. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно заменив все знаки пунктуации на знак «!».

# переменные
marks = '''!()-[]{};?@#$%:'"\,./^&amp;*_'''

# функции
def count_upper(Str):
  count = 0
  for i in range(len(Str)):
    if Str[i].isupper():
      count += 1
  return count

def replacement_signs(Str):
  for i in range(len(Str)):
    if Str[i] in marks:
      Str = Str.replace(Str[i], '!')
  return Str

# программа
file_one = open("бородино.txt", "r")
str_text = file_one.read()
print("<----------содержимое первого файла---------->")
print(str_text)
print("<-------------------------------------------->")
print(f"количество букв в верхнем регистре: {count_upper(str_text)}\n")
file_one.close()

file_two = open("new_file.txt", "w")
file_two.writelines(replacement_signs(str_text))
file_two.close()

file_two = open("new_file.txt", "r")
print("<----------содержимое второго файла---------->")
print(file_two.read())
print("<-------------------------------------------->")
file_two.close()