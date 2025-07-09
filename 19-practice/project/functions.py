from file_manager import write_to_file, write_to_json, writerows

def get_info():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    file_type = input("Enter file type: ")

    if file_type.endswith(".txt"):
        write_to_file(name, email)
    elif file_type.endswith(".json"):
        write_to_json(name, email)
    elif file_type.endswith(".csv"):
        writerows(name, email)


