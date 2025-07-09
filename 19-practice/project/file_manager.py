import os, json, csv

def write_to_file(name, email):
    data = f"User: {name}\nEmail: {email}\n"
    with open(file="users_file.txt", mode="w") as file:
        file.write(data)


def write_to_json(name, email):
    data = {
        "name" : name,
        "email": email
    }
    with open("users_js.json", mode="w") as file:
        json.dump(data, file, indent=4)


def writerows(name, email) -> None:
    data = list()
    data.append(name)
    data.append(email)
    with open(file="users_cs.csv", mode="w", encoding="UTF-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

def read() -> list:
    if os.path.exists(path=path):
        with open(file=path, mode="r", encoding="UTF-8", newline="") as file:
            reader = csv.reader(file)
            return list(reader)
    return list()