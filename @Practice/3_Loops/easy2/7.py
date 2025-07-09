"""Quyidagi shaklni yasang, for bilan"""


rows = 5
cols = 5

for i in range(rows):
    for j in range(cols):
        # Har bir qatordagi birinchi raqam (0 yoki 1) i ga bog‘liq
        print((i + j) % 2, end=" ")
    print()
