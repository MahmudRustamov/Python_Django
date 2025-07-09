"""
Ushbu kichik dasturni yaratish kerak:
Uning maqsadi bozorlik ro'yxatini tuzishimga yordam bersin.
Ma'lumotlarni products.json nomli faylda saqlasin
va unda quyidagi imkoniyatlar bo'lsin

Menu:
    1. Ro'yxatni ko'rish
    2. Yangi mahsulot qo'shish | nomi va qancha olish kerakligini kiritiadi
    3. O'chirib tashlash | mahsulotni nomini kiritadi va uni fayldan o'chirib tashlaysiz
    4. Butun faylni tozalash
    5. Chiqish
"""
from functions import add_product, view_products, delete_product, clear_file

def main():
    while True:
        print("""
        1. View Products
        2. Add a New Product
        3. Delete a Product
        4. Clear File
        5. Exit
        """)
        choice = int(input("Enter your choice: "))

        if choice == 1:
            view_products()
        elif choice == 2:
            add_product()
        elif choice == 3:
            delete_product()
        elif choice == 4:
            clear_file()
        elif choice == 5:
            print("Exciting the program")
            return
        else:
            print("Invalid choice")
        return main()


if __name__ == "__main__":
    main()