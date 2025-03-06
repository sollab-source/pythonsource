class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("이 동물은 소리를 낼 수 있습니다.")

# 자식 클래스 (Animal을 상속받음)
class Dog(Animal):
    def speak(self):
        print(f"{self.name}가 멍멍! 하고 짖습니다.")

class Cat(Animal):
    def speak(self):
        print(f"{self.name}가 야옹~ 하고 웁니다.")

# 객체 생성
dog = Dog("바둑이")
cat = Cat("나비")
dog.speak()  
cat.speak()  
