"""Foydalanuvchidan N, M va K sonlarini qabul qiling.
N dan M gacha K ta juft sonning yig'indisini hisoblovchi dastur tuzing"""

try:
    n = int(input("Enter n: "))
    m = int(input("Enter m: "))
    k = int(input("Enter k: "))
    evens = 0
    for num in(range(n, m)):
        if num % 2 == 0:
            evens += 1

    if evens >= k:
        even_nums = 0
        counter = 0
        for num in(range(n, m)):
            if num % 2 == 0 and counter < k:
                even_nums += num
                counter += 1
        print("Sum: ", even_nums, counter)
    else:
        print("There are not enough even numbers in this range!!!")

except ValueError:
    print("You should enter only numbers!!!")