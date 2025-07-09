def save_results(num1, num2, sign, result):
    with open ("results.txt", "a") as file:
        file.write(f"{num1} {sign} {num2} = {result}\n")


def read_file():
    with open("results.txt", "r") as file:
        data = file.read()
        print(f"Calculator history\n{data}")


def clear_data():
    with open("results.txt", "w") as file:
        pass
    return f"All history cleared!!"


def addition(a, b):
    result = a + b
    save_results(a, b, '+', result)
    return f"Result -> {result}"


def subtraction(a, b):
    result = a - b
    save_results(a, b, '-', result)
    return f"Result -> {result}"


def multiplication(a, b):
    result = a*b
    save_results(a, b, '*', result)
    return f"Result -> {result}"


def division(a, b):
    if b != 0:
        result = a / b
        save_results(a, b, '/', result)
        return f"Result -> {result}"
    else:
        return "Cannot divide by zero"
