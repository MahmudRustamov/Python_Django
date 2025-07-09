"""10 dan N gacha bo`lgan natural sonlar berilgan. 5 ga karrali bo`lgan
toq sonlari chop eting"""
res = 0
num = int(input('Enter a number: '))
if num > 10:
    count = 10
    while count <= num:
        if count % 5 == 0 and count % 2 == 1:
            res += 1
            print(count) 
        count += 5
else:
    print("Number should be greater than 10")

if res == 0:
    print('There are no odd nums to divide by 5 ')