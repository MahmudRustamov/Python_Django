import csv
import os
from abc import ABC, abstractmethod

class FileHandler:
    @abstractmethod
    def write():
        pass

    
    def read():
        pass


class JSON(ABC):
    def __init__(self, filename):
        self.filename = f"{filename}.json"
        self.path = f"data/{filename}.json"


    def write(self, data: list):
        with open(file=self.path, mode="w", encoding="UTF-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)



    def read(self):
        if os.path.exists(path=self.path):
            with open(file=self.path, mode="r", encoding="UTF-8", newline="") as file:
                reader = csv.reader(file)
                return list(reader)
        return list()
    

class CSV(ABC):
    def __init__(self):
        super().__init__()


    def write(self, data: list[list]) -> None:
        with open(file=self.path, mode="w", encoding="UTF-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)


    def read(self) -> list:

        if os.path.exists(path=self.path):
            with open(file=self.path, mode="r", encoding="UTF-8", newline="") as file:
                reader = csv.reader(file)
                return list(reader)
        return list()



class Text(ABC):
    def __init__(self):
        super().__init__()


    def read(self):
        with open(self.path, "r") as file:
            data = file.read()
            print(f"Calculator history\n{data}")


    def write(self):
        if os.path.exists(self.path):
            text = input("Enter your text: ")
            with open(file = self.path, mode = "w") as file:
                file.write(text)
                print("Your text is saved!!!")
        else:
            print("File not found!!!")

