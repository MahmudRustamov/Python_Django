import csv
import os

class FileManager:
    def __init__(self, filename):
        self.filename = f"{filename}.json"
        self.path = f"data/{filename}.json"


    def writerows(self, data: list):
        with open(file=self.path, mode="w", encoding="UTF-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)

    
    def append(self, data: list):
        with open(file=self.path, mode="w", encoding="UTF-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(data)


    def read(self):
        if os.path.exists(path=self.path):
            with open(file=self.path, mode="r", encoding="UTF-8", newline="") as file:
                reader = csv.reader(file)
                return list(reader)
        return list()