class RentCar:
    def __init__(self,car_name, car_model):
        self.car_name = car_name
        self.car_model = car_model
        self.__is_rented = False



    @property
    def car_rented(self):
        return "car is rented"


    @car_rented.setter
    def car_rented(self, option):
        self.__is_rented = option
        
    

    def rent_car(self, model):
        if model == self.car_model:
            if self.is_rented():
                return ("You can not rent this car")  
            elif not self.is_rented():
                self.car_rented = True
                return f"{self.car_name} {self.car_model} {self.car_rented}"
            else:
                print("Car is not found")


    def return_car(self, model):
        if model == self.car_model:
            if self.is_rented():
                self.car_rented = False
                return f"{self.car_name} {self.car_model} is returned"
            else:
                print("Car is not found")
    

    def is_rented(self):
        return self.__is_rented
    

car = RentCar("BMW", "M5")
print(car.rent_car("M5"))
# print(car.return_car("M5"))
print(car.is_rented())
    