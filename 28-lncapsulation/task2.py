"""# 2-vazifa: Pythonic getter/setter
# Yuqoridagi Book klassida @property va @setter orqali title ni boshqaring."""

class Book:
    def __init__(self, title):
        self.__title = title

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        self.__title = new_title


book = Book("New years")
book.title = "Hello"
print(book.title)