text = "ABCDEFGHIJ"
#       0123456789  (인덱스)

# 스텝 1 (기본값) - 모든 문자 선택
print(text[0:10:1])  # ABCDEFGHIJ
# 위와 동일한 결과
print(text[::1])     # ABCDEFGHIJ

# 스텝 2 - 인덱스 0, 2, 4, 6, 8의 문자 선택
print(text[0:10:2])  # ACEGI
# 위와 동일한 결과
print(text[::2])     # ACEGI

# 스텝 3 - 인덱스 0, 3, 6, 9의 문자 선택
print(text[0:10:3])  # ADGJ
# 위와 동일한 결과
print(text[::3])     # ADGJ

# 음수 스텝 사용 - 문자열 뒤집기
print(text[::-1])    # JIHGFEDCBA

# 음수 스텝으로 역순 간격 지정
print(text[::-2])    # JHFDB (끝에서부터 2칸 간격으로)