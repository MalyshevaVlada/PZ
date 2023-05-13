# Создайте класс «Книга», который имеет атрибуты название, автор и количество
# страниц. Добавьте методы для чтения и записи книги.

class book:
  # constructor
  def __init(self, name: str, autor: str, count_page: int):
    self.__name_book = name
    self.__autor_book = autor
    self.__count_page_book = count_page

  # destructor
  def __del__(self):
    pass

  # set
  def set_name(self, name: str):
    self.__name_book = name

  def set_autor(self, autor: str):
     self.__autor_book = autor

  def set_count_page(self, count_page: int):
    self.__count_page_book = count_page

  # get
  def get_name(self) -> str:
    return self.__name_book

  def get_autor(self) -> str:
    return self.__autor_book

  def get_count_page_book(self) -> str:
    return self.__count_page_book
