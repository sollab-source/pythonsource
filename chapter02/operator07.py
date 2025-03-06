a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True (내용이 같음)
print(a is b)  # False (다른 객체)
x = 5
y = 5
print(x is y)  # True (작은 정수는 메모리에 캐싱됨)
# None 비교 시 is 사용이 권장됨
value = None
print(value is None)  # True (올바른 방법)
print(value == None)  # True (작동하지만 권장되지 않음)