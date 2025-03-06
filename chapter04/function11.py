#1 매개변수도 있고, 반환값도 있는 함수
def add(a, b):
    return a + b

result = add(3, 4)
print(result)  # 7

#2 매개변수는 있지만, 반환값이 없는 함수
def greet(name):
    print(f"안녕하세요, {name}님!")

greet("홍길동")  # 안녕하세요, 홍길동님!

#3 매개변수도 없고, 반환값도 없는 함수
def say_hello():
    print("Hello!")

say_hello()  # Hello!



