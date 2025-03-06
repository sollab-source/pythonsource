#1 % 연산자 사용

name = "홍길동"
age = 30
print("이름: %s, 나이: %d" % (name, age))  # 이름: 홍길동, 나이: 30

'''
주요 포맷 지정자:
%s: 문자열
%d: 정수
%f: 실수
%c: 문자 1개
%.2f: 소수점 둘째 자리까지의 실수
'''

#2 format() 메서드 사용

name = "홍길동"
age = 30
print("이름: {}, 나이: {}".format(name, age))  # 이름: 홍길동, 나이: 30

# 인덱스 지정
print("이름: {0}, 나이: {1}".format(name, age))  # 이름: 홍길동, 나이: 30
print("나이: {1}, 이름: {0}".format(name, age))  # 나이: 30, 이름: 홍길동

# 이름 지정
print("이름: {name}, 나이: {age}".format(name=name, age=age))  # 이름: 홍길동, 나이: 30