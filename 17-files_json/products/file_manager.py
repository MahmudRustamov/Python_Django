import json
import os.path


def write_to_json(file: str, data: list):
    if os.path.exists(file):
        with open(file = file, mode = "w") as file:
            json.dump(data, file, indent = 4)


def read_from_json(file):
    if os.path.exists(file) and os.path.getsize(file) > 0:
        with open(file = file, mode = "r") as file:
            return json.load(file)
    return []


info = [
  {
    "name": "apples",
    "quantity": 5
  },
  {
    "name": "milk",
    "quantity": 2
  },
  {
    "name": "bread",
    "quantity": 1
  }
]

