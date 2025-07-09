import csv
import json
import os

class FileHandler:
    def __init__(self, filename, file_type):
        self.filename = filename
        self.file_type = file_type

    def read(self):
        pass



class TextFileHandler(FileHandler):
    def __init__(self, filename, file_type):
        super().__init__(filename, file_type)


    def read(self):
        with open(f"{self.filename}.txt", "r") as file:
            data = file.read()
            return data



class CSVFileHandler(FileHandler):
    def __init__(self, filename, file_type):
        super().__init__(filename, file_type)


    def read(self):

        with open(file=f"{self.filename}.csv", mode="r", encoding="UTF-8", newline="") as file:
            reader = csv.reader(file)
            return list(reader)
        

class JSONFileHandler(FileHandler):


    def __init__(self, filename, file_type):
        super().__init__(filename, file_type)


    def read(self):
        if os.path.exists(path=f"{self.filename}.json") and os.path.getsize(file) > 0:
            with open(file=f"{self.filename}.json", mode="r") as file:
                return json.load(file)
        return []
