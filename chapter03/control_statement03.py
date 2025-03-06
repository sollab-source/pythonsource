''' 
# if-elif-else 문 구조
if 조건1:
    # 조건1이 참일 때 실행할 코드
elif 조건2:
    # 조건1이 거짓이고, 조건2가 참일 때 실행할 코드
elif 조건3:
    # 조건1, 조건2가 거짓이고, 조건3이 참일 때 실행할 코드
else:
    # 모든 조건이 거짓일 때 실행할 코드
'''
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"점수: {score}, 학점: {grade}")