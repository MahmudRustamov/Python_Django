""" 1-vazifa: Oddiy inkapsulyatsiya
# Book klassini yarating, unda private atribut __title bo‘lsin.
# get_title() va set_title() metodlari orqali o‘qish va o‘zgartirish imkonini yarating."""


class Book:
    def __init__(self, title):
        self.__title = title


    def get_title(self):
        return self.__title


    def set_title(self, new_title):
            self.__title = new_title


book = Book("New years")
book.set_title("Hello")
print(book.get_title())
