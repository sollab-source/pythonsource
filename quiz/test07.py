class Car:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

    def display_info(self):
        print(f"브랜드: {self.brand}, 색상: {self.color}, 연식: {self.year}")

# 객체 생성 및 출력
car1 = Car("Hyundai", "Red", 2022)
car2 = Car("Tesla", "White", 2023)

car1.display_info()
car2.display_info()