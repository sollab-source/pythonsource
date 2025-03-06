def introduce(name="익명"):
    print(f"안녕하세요, 저는 {name}입니다.")

introduce()  # 안녕하세요, 저는 익명입니다.
introduce("홍길동")  # 안녕하세요, 저는 홍길동입니다.

# 여러 개의 매개변수에 기본값 지정
def register(name="손님", age=20, nationality="한국"):
    print(f"이름: {name}, 나이: {age}, 국적: {nationality}")

register()  # 이름: 손님, 나이: 20, 국적: 한국
register("김철수")  # 이름: 김철수, 나이: 20, 국적: 한국
register("박영희", 25)  # 이름: 박영희, 나이: 25, 국적: 한국
register("John Smith", 30, "미국")  # 이름: John Smith, 나이: 30, 국적: 미국