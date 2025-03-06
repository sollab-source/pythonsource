try:
    num = int(input("숫자를 입력하세요: "))
    print(10 / num)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다!")
except ValueError:
    print("올바른 숫자를 입력하세요!")
except Exception as e:
    print(f"오류 발생: {e}")
finally:
    print("예외 처리 완료!")
