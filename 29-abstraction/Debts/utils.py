from file_manager import FileManager
from datetime import datetime


class MarketDebts:
    def __init__(self, name, phone_number, debt, comment):
        self.phone_number = phone_number
        self.name = name
        self.debt = debt
        self.comment = comment
        self.time = datetime.now()
        self.debt_data = FileManager("debts")


    def all_debts(self):
        debt_data = self.debt_data.read()
        if debt_data:
            for debt in debt_data:
                print(f"Phone: {debt[0]}  Name: {debt[1]}  Debt: {debt[2]}  Comment: {debt[3]}  Date: {debt[4]}")
        else:
            print("Data not found!!")


    def add_debt(self):
        data = [self.phone_number, self.name, self.debt, self.comment, self.time]
        self.debt_data.append(data)
        print("New debt is added!!!")


    def search_person(self):
        phone = input("Enter customer's phone number: ").strip()
        debts = self.debt_data.read()
        if debts:
            for debt in debts:
                if debt[0].strip() == phone:
                    print(f"Phone: {debt[0]}  Name: {debt[1]}  Debt: {debt[2]}  Comment: {debt[3]}  Date: {debt[4]}")
        else:
            print("Data not found!!")


    def delete_debt(self):
        phone = input("Enter customer's phone number: ").strip()
        debts = self.debt_data.read()
        if debts:
            is_found = False
            for index, debt in enumerate(debts):
                if debt[0].strip() == phone:
                    debts.pop(index)
                    is_found = True
                    break


            if is_found:
                self.debt_data.writerows(debts)
                print("Debt is deleted!!!")           
        else:
            print("Data not found!!")