"""10. [8,9,10] royxat berilgan. Quyidagilarni bajaring:
    
    (a) ikkinchi sonni orniga 17 ni saqlang
    
    b) ro'yxat oxiriga 4, 5 va 6 sonlarini qo'shing
    
    (c) ro'yxatdagi birinchi sonni olib tashlang
    
    (d) ro'yxatni saralang
    
    (e) ro'yxat elementlarini har birini ikkiga kopaytiring
    
    (f) 3 -songa 25 ni qo'shing"""


ls = [8,9,10]

# """(a) ikkinchi sonni orniga 17 ni saqlang"""
# print(ls)
# ls[1] = 17
# print(ls)

# """(b) ro'yxat oxiriga 4, 5 va 6 sonlarini qo'shing"""
# print(ls)
# nums = [4, 5, 6]
# ls.extend(nums)
# # ls.append(4)
# # ls.append(5)
# # ls.append(6)
# print(ls)

# """(c) ro'yxatdagi birinchi sonni olib tashlang"""
# print(ls)
# ls.pop(0)
# # del ls[0]
# print(ls)


# """(d) ro'yxatni saralang"""
# print(ls)
# ls.sort(reverse=True)
# print(ls)


"""(e) ro'yxat elementlarini har birini ikkiga kopaytiring"""
kvadratlar_listi = list(map(lambda x: x + 2,  ls))
print(kvadratlar_listi)


# """ (f) 3 -songa 25 ni qo'shing"""
# print(ls)
# ls[-1] += 25
# print(ls) 