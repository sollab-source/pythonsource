'''
# 조건부 표현식 구조
값1 if 조건 else 값2
'''
age = 20
status = '성인' if age >= 18 else '미성년자'
print(status)  # 성인

#위 코드는 아래의 if-else 구문과 동일

if age >= 18:
    status = '성인'
else:
    status = '미성년자'