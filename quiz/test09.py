with open("my_data.txt", "w", encoding="utf-8") as file:
    while True:
        text = input("저장할 내용을 입력하세요 (종료하려면 '종료' 입력): ")  
        if text == "종료":  
            break
        file.write(text + "\n")
