# составить генератор (yield), который переведёт
# символы строки из нижнего регистра в верхний

# -> qwertyuiop
# <- QWERTYUIOP

def my_upper(m_str):
  yield from [i.upper() for i in m_str]

Str = input("Enter string: ")
print(f"before: {Str}")
new_str = my_upper(Str)

print("after: ", end='')
for char in new_str:
  print(char, end='')