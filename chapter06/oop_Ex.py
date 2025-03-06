class Car:
    def __init__(self, brand, color):
        self.brand = brand  
        self.color = color  
    
    def drive(self):  
        print(f"{self.color} {self.brand} 자동차가 달립니다!")


my_car = Car("BMW", "빨간색")
print(my_car.brand)  
print(my_car.color)  
my_car.drive()  
