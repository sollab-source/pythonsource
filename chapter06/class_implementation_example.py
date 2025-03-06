# 6-2 클래스 구현 예제

# 학생 클래스 정의
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"안녕하세요! 저는 {self.name}이고, {self.age}살입니다.")

# 객체 생성
student1 = Student("이쁜이", 18)
student2 = Student("철수", 20)

student1.introduce()  # "안녕하세요! 저는 이쁜이이고, 18살입니다."
student2.introduce()  # "안녕하세요! 저는 철수이고, 20살입니다."
