#1 리스트 생성
numbers = [1, 2, 3, 4, 5]  # 정수 리스트
mixed = [1, "Hello", 3.14, True]  # 혼합 자료형 리스트
empty = []  # 빈 리스트

#2 리스트 접근
print(numbers[0])  # 1 (첫 번째 요소)
print(numbers[-1])  # 5 (마지막 요소)

#3 리스트 조작
numbers.append(6)  # 끝에 요소 추가
print(numbers)  # [1, 2, 3, 4, 5, 6]

numbers.insert(0, 0)  # 특정 위치에 요소 삽입 (인덱스, 값)
print(numbers)  # [0, 1, 2, 3, 4, 5, 6]

numbers.remove(3)  # 값이 3인 첫 번째 요소 제거
print(numbers)  # [0, 1, 2, 4, 5, 6]