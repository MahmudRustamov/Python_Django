import csv
import os.path


def write_to_csv(filename: str, data: list):
    with open(file = filename, mode = "w", encoding="UTF-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)



def read_csv(filename: str):
    try:
        with open(file = filename, mode = "r", encoding="UTF-8", newline="") as file:
            reader = csv.reader(file)
            return list(reader)
    except Exception as error:
        return error

