#1 문자열을 정수나 실수로 변환
num_str = "100"
num_int = int(num_str)  # 문자열 -> 정수 변환
num_float = float(num_str)  # 문자열 -> 실수 변환
print(num_int, num_float)  # 100 100.0

#2 숫자를 문자열로 변환
num = 42
str_num = str(num)  # 정수 -> 문자열 변환
print(str_num, type(str_num))  # "42" <class 'str'>

#3 리스트와 튜플 간 변환
my_list = [1, 2, 3]
my_tuple = tuple(my_list)  # 리스트 -> 튜플 변환
print(my_tuple)  # (1, 2, 3)
new_list = list(my_tuple)  # 튜플 -> 리스트 변환
print(new_list)  # [1, 2, 3]

#4 문자열을 리스트로 변환
str_to_list = list("Python")
print(str_to_list)  # ['P', 'y', 't', 'h', 'o', 'n']

#5 변환할 수 없는 형식으로 시도하면 ValueError가 발생
# 오류 예시
# int("Hello")  # ValueError: invalid literal for int() with base 10: 'Hello’
'''
해당 코드의 오류는 숫자로 변환할 수 없는 문자열을 int()에 전달했을 때 발생한다. 
int() 함수는 문자열이 숫자 형태일 때만 변환이 가능하며, 알파벳이나 특수문자가 포함된 경우 변환할 수 없다.
'''