"""
Ushbu classni yarating
Class Concert: author, date, total_tickets, price
Methods:
    get_price()
    get_full_info()
    save_to_file()
    read_data()

    optional
    buy_ticket(phone_number, full_name, quantity)

"""


import csv
import os


class Concert:
    def __init__(self, filename, author,date,total_tickets, price):
        self.filename = filename
        self.author = author
        self.date = date
        self.total_tickets = total_tickets
        self.price = price


    def get_price(self):
        return self.price


    def get_full_info(self):
        return f"Author: {self.author}\nDate: {self.date}\nPrice: {self.price}\nTotal Tickets: {self.total_tickets}"


    def read_data(self):
        path = f"data/{self.filename}.csv"
        if os.path.exists(path=path):
            with open(file=path, mode="r", encoding="UTF-8", newline="") as file:
                reader = csv.reader(file)
                for concert in reader:
                    return f"Author: {concert[0]}\nDate: {concert[1]}\nPrice: {concert[2]}\nTotal Tickets: {concert[3]}"
        return None



    def save_to_file(self) -> None:
        path = f"data/{self.filename}.csv"
        data = [self.author, self.date, self.total_tickets, self.price]
        with open(file=path, mode="a", encoding="UTF-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(data)
            print("Data is added!!!")


author1 = input("Author: ")
date1 = input("Date: ")
price1 = input("Price:")
total_tickets1 = input("Total tickets: ")
concert1 = Concert(filename="concert", author=author1, date=date1, price=price1, total_tickets=total_tickets1)

while True:
    print("""
            1. Save data
            2. Price
            3. Show full info
            4. Read all data
            5. Exit
            """)
    choice = input("Enter your choice: ")

    if choice == "1":
        concert1.save_to_file()
    elif choice == "2":
        print("Ticket Price: ", concert1.get_price())
    elif choice == "3":
        print(concert1.get_full_info())
    elif choice == "4":
        print(concert1.read_data())
    elif choice == "5":
        print("Good Bye!!!")
        break
    else:
        print("Invalid choice!!!")