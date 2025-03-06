# 문자열 생성
greeting = "Hello, Python!"
print("원본 문자열:", greeting)

# 인덱싱: 첫 번째 문자에 접근 (0부터 시작)
first_char = greeting[0]  
print("첫 번째 문자:", first_char)
last_char = greeting[-1]  # '!'
print("마지막 문자:", last_char)

# 슬라이싱: 7번째 문자부터 끝까지
substring = greeting[7:]
print("슬라이스:", substring)

# 문자열 메서드 사용: 모두 대문자로 변환
upper_greeting = greeting.upper()  
print("대문자 문자열:", upper_greeting)