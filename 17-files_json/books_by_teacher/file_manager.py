import json
import os.path

data = {
    ty[e]
}
def write_to_json(file: str, data: list):
    with open(file=file, mode="w") as file:
        json.dump(data, file, indent=4)


def read_from_json(file: str):
    if os.path.exists(path=file) and os.path.getsize(file) > 0:
        with open(file=file, mode="r") as file:
            return json.load(file)
    return []
