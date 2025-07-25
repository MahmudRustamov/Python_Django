"""Quyidagi arraydan nusxa oling va olingan nusxani juft indexdagilarni 2 chi darajaga ko'tarib,
toq indexdagilarni kubga ko'tarib nusxalangan arrayga o'zlashtirib 
dastlabki va nusxa olingan arrayni ekranga chiqaring"""


numbers = [7, 8, 1, 3, 4, 6, 7, 5]
updated_numebrs = list()

for i in range(len(numbers)):
    if i % 2 == 0:
        updated_numebrs.append(numbers[i] ** 2)
    else:
         updated_numebrs.append(numbers[i] ** 3)
print(updated_numebrs)