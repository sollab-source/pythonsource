x = 10

def wrong_change_x():
    x = 20  # 이것은 새로운 지역 변수 x를 생성함
    print("함수 내부 x:", x)  # 20 (지역 변수)

wrong_change_x()
print("전역 변수 x:", x)  # 10 (전역 변수는 변경되지 않음)