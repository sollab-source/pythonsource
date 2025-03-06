# 구구단 출력 (for 문 안에 while 문 사용)
for i in range(2, 10):
    j = 1
    while j < 10:
        print(f"{i} x {j} = {i * j}")
        j += 1
    print()  # 각 단 사이에 빈 줄 출력