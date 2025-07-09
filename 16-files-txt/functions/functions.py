import os 

def create_file():
    name = input("Enter file name: ")
    if not os.path.exists(name):
        with open(file=name, mode="x") as file:
            print("File is created")
    else:
        print("File exists. Try with another name")

def delete_file():
    name = input("Enter the name of the file to remove: ")
    if os.path.exists(name):
        os.remove(name)
    else:
        print("File does not exist")


def check_file():
    name = input("Enter file's name to check: ")
    if os.path.exists(name):
        print( "File exists")
    else:
        print("File does not exist")


def write_to_file():
    name = input("Enter file name: ")
    if os.path.exists(name):
        text = input("Enter your text: ")
        with open(file = name, mode = "w") as file:
            file.write(text)
            print("Your text is saved!!!")
    else:
        print("File not found!!!")



def append_to_file():
    name = input("Enter the file name: ")
    if os.path.exists(name):
        text = input("Enter your text: ")
        with open(file = name, mode = "a") as file:
            file.write(f"\n{text}")
            print("Your text is saved!!!")
    else:
        print("We could not find the file!!!")


def read_file():
    name = input("Enter the file name: ")
    if os.path.exists(name):
        with open(file = name, mode = "r") as file:
            data = file.read()
            print(f"--------------------\n{data}\n--------------------")
    else:
        print("File is not found...")

    
