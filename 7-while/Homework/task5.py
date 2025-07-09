while True:
    num1 = int(input("a= "))
    num2 = int(input("b= "))

    sign = input("To break enter <stop> Enter a sign:(+, -, *, /) ").lower()
    if sign == "+":
        print(f"Result -> {num1 + num2}")
    elif sign == "-":
        print(f"Result -> {num1 - num2}")
    elif sign == "*":
        print(f"Result -> {num1 * num2}")
    elif sign == "/":
        print(f"Result -> {num1 / num2}")
    elif sign == "stop":
        break
