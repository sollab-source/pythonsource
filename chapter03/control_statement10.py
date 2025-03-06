# 사용자가 'q'를 입력할 때까지 계속 입력 받기
while True:
    user_input = input("메시지를 입력하세요 (종료: q): ")
    if user_input == 'q':
        break
    print(f"입력한 메시지: {user_input}")
print("프로그램 종료")