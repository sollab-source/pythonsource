# 1부터 10까지의 숫자 중 홀수만 출력
for i in range(1, 11):
    if i % 2 == 0:  # 짝수면 건너뛰기
        continue
    print(i)  # 1, 3, 5, 7, 9 출력