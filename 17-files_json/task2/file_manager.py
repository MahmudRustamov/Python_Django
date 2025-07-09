import json, os


def write_to_json(file: str, data: list):
    with open(file = file, mode="w") as file:
        json.dump(data, file, indent = 4)


def read_from_json(file):
    if os.path.exists(file):
        if os.path.getsize(file) > 0:
            with open(file= file, mode="r") as file:
                return json.load(file)
        else:
            return "File is empty"
    else:
        return "File not found"

# write_to_json()
print(read_from_json("test.json"))


