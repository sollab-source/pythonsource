x = 10  # 전역변수

def my_func():
    y = 5  # 지역변수
    print(y)

my_func()  # 5
print(x)  # 10
print(y)  # 오류 발생 (y는 함수 안에서만 존재)