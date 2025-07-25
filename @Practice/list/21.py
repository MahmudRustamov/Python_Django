def rotate_list_manual(arr):
    if not arr:  # Agar list bo'sh bo'lsa, hech narsa qilmaymiz
        return []

    last_element = arr[-1]  # Oxirgi elementni saqlab olamiz

    # Listdagi elementlarni oxiridan boshiga qarab bir pozitsiya o'ngga suramiz
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = last_element  # Saqlab qo'ygan oxirgi elementni birinchi o'ringa qo'yamiz
    return arr

# Misol
my_list = [3, 4, 5, 6]
print(f"Boshlang'ich ro'yxat: {my_list}")
rotated_list = rotate_list_manual(my_list)
print(f"Aylantirilgan ro'yxat: {rotated_list}") # Natija: [6, 3, 4, 5]