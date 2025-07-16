"""Kiritilgan ro'yxatda qancha juft raqam borligini chop eting."""

ls = [95, 50, 36, 4, 67, 97, 8, 80, 85, 3, 92, 14, 19, 54, 38, 80, 2, 18, 30, 93]

evens, odds = 0, 0

for i in ls:
    if i % 2 == 0:
        evens += 1
    else:
        odds += 1

print("Number of evens: {}\nNumber of odds: {}".format(evens, odds))