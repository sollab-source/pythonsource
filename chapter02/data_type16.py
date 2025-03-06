# 튜플 생성
coordinates = (10, 20)  # 단순 튜플
person = ("John", 25, "New York")  # 혼합 자료형 튜플
single_item = (42,)  # 요소가 하나인 튜플은 반드시 콤마가 필요
empty_tuple = ()  # 빈 튜플

# 튜플 접근 (리스트와 동일)
print(coordinates[0])  # 10
print(coordinates[1])  # 20

# 튜플은 수정 불가능
# coordinates[0] = 100  # TypeError: 'tuple' object does not support item assignment
tuple_data = (10, 20, 30)
print(tuple_data[1])  # 20