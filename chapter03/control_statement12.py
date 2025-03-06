# for-else 구문 예시
for i in range(1, 6):
    print(i)
else:
    print("반복 완료!")
# while-else 구문 예시
count = 1
while count <= 5:
    print(count)
    count += 1
else:
    print("반복 완료!")

## break 문이 실행되면 else 블록은 실행되지 않는다.

# 숫자 1부터 10까지 검사하여 5를 찾으면 중단
for i in range(1, 11):
    print(f"검사 중: {i}")
    if i == 5:
        print("5를 찾았습니다!")
        break
else:
    print("5를 찾지 못했습니다.")