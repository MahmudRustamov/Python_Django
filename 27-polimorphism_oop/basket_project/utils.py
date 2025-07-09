import json, os

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        if os.path.getsize(filename=self.filename) > 0:
            with open(file=self.filename, mode="r", encoding="UTF-8") as file:
                return json.load(file)
        else:
            return list()

    def write_file_basket(self, data: list):
        with open(file=self.filename, mode="w", encoding="UTF-8") as file:
            return json.dump(data, file, indent=4)