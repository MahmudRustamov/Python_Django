from functions import addition, subtraction, multiplication
from functions import division, read_file, clear_data

def main():
    while True:
        print("""Welcome to Calculator
        1. Add
        2. Subtract
        3. Multiply
        4. Divide
        5. Show all results
        6. Exit or clear history""")
        sign = int(input("Enter your choice: "))

        if sign == 5:
            read_file()
        elif sign == 6:
            choice = input("e -> Exit  or  c -> clear history: ").lower()
            if choice == "e":
                print("Thank you for using Calculator!!")
                break
            elif choice == "c":
                print(clear_data())
            else:
                print("Invalid choice!!!")
        elif sign in [1, 2, 3, 4]:
            num1 = int(input("a= "))
            num2 = int(input("b= "))
            if sign == 1:
                print(addition(num1, num2))
            elif sign == 2:
                print(subtraction(num1, num2))
            elif sign == 3:
                print(multiplication(num1, num2))
            elif sign == 4:
                print(division(num1, num2))
        else:
            print("Invalid choice!!!")


if __name__ == "__main__":
    main()