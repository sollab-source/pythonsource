try:
    num = int(input("숫자를 입력하세요: "))
    result = 100 / num
    print(f"결과: {result}")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다!")
except ValueError:
    print("올바른 숫자를 입력하세요!")
except Exception as e:
    print(f"예외 발생: {e}")
