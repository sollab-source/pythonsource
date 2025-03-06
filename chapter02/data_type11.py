#1 양수 인덱스
text = "Python"
#       012345  (인덱스 번호)
# 첫 번째 문자 접근 (인덱스 0)
first_char = text[0]
print(first_char)  # P
# 세 번째 문자 접근 (인덱스 2)
third_char = text[2]
print(third_char)  # 

#2 음수 인덱스
text = "Python"
#       0  1  2  3  4  5   (양수 인덱스)
#       P  y  t  h  o  n
#      -6 -5 -4 -3 -2 -1   (음수 인덱스)
# 마지막 문자 접근 (인덱스 -1)
last_char = text[-1]
print(last_char)  # n

# 마지막에서 두 번째 문자 접근 (인덱스 -2)
second_last_char = text[-2]
print(second_last_char)  # o

#3 인덱싱에서 범위를 벗어난 인덱스를 사용하면 IndexError가 발생
'''
# 6글자인 'Python'에서 인덱스 6 접근 시도
print(text[6])  # IndexError: string index out of range
'''