text = "Python Programming"
#       0123456789...

# 인덱스 0부터 5번 인덱스 전까지 (0,1,2,3,4) 추출
substring1 = text[0:5]
print(substring1)  # Pytho

# 시작 인덱스가 생략되면 처음(0)부터 시작
substring2 = text[:5]
print(substring2)  # Pytho

# 끝 인덱스가 생략되면 끝까지 포함
substring3 = text[7:]
print(substring3)  # Programming

# 처음부터 끝까지 (전체 문자열 복사)
substring4 = text[:]
print(substring4)  # Python Programming