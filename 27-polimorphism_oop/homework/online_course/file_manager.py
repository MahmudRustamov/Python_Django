import json
import os

class FileManager:
    def __init__(self, filename):
        self.filename = f"{filename}.json"
        self.path = f"data/{filename}.json"


    def write(self, data: list):
        with open(file=self.path, mode="w", encoding="UTF-8") as file:
            return json.dump(data, file, indent=4)


    def read(self):
        try:
            if os.path.getsize(filename=self.path) > 0:
                with open(file=self.path, mode="r", encoding="UTF-8") as file:
                    return json.load(file)
            else:
                return list()
        except FileNotFoundError:
            return list()