x = 10

def change_x():
    global x  # 전역 변수 사용 선언
    x = 20

change_x()
print(x)  # 20