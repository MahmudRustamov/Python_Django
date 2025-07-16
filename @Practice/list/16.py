""""Bir xil o'lchamdagi L va M bolgan har qanday ikkita ro'yxatni oladigan 
va ularning elementlarini qo'shib, yangi N royxat hosil qiling."""

try:
    
    ls1 = [1, 5, 7, 89, 0, 3]
    ls2 = [56, 78, 2, 7, 23, 6, 8]
    ls3 = []

    for i in range(len(ls2)):
        ls3.append(ls1[i] + ls2[i])

    print(ls3)
except IndexError:
    print("The length of two lists should be the same!!")