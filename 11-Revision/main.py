"""population projectga o'xshash , faqat shuni cars = [] list uchun qilib kelasiz.
Car => name , color , price , year"""

cars = []

while input('Do you wanna add a car(yes/no) ?:').startswith('y'):

    car_name = input('Car Name : ')
    year = int(input('Year : '))
    color = input('Color: ')
    price = input('Price : ')
    car_info = (car_name, year, color, price)
    cars.append(car_info) 
    
else:
    choice = input('Do you want to see cars list (yes/no) ?: ')
    if choice == 'yes':
        for car in cars:
            print(car)
    else:
        print('Come back again 😊')
