#1 딕셔너리 생성
person = {'name': '홍길동', 'age': 30, 'city': '서울'}
empty_dict = {}  # 빈 딕셔너리

#2 딕셔너리 접근
print(person['name'])  # 홍길동
print(person.get('age'))  # 30 (.get() 메서드로도 접근 가능)

#3 딕셔너리 항목 추가/수정
person['job'] = '개발자'  # 새 항목 추가
print(person)  # {'name': '홍길동', 'age': 30, 'city': '서울', 'job': '개발자'}
person['age'] = 31  # 기존 항목 수정
print(person)  # {'name': '홍길동', 'age': 31, 'city': '서울', 'job': '개발자'}

#4 딕셔너리 항목 삭제
del person['city']  # 항목 삭제
print(person)  # {'name': '홍길동', 'age': 31, 'job': '개발자'}

#5 키 존재 여부 확인
print('name' in person)  # True
print('address' in person)  # False
