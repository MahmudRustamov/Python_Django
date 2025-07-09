"""Rostlikka tekshiring. Foydalanuvchi kiritgan sonning(aniq 3 xonali) 
raqamlar yig'indisidan 1 ni ayirsa qolgan raqam toq son."""

digit = input("N = ")
result = 0

if len(digit) == 3: 
    for num in digit:
        result += int(num)
        
    if (result-1) % 2 == 0:
        print(True)
    else:
        print(False)   
else:
    print("Enter a 3 digit number")


