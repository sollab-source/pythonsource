with open("example.txt", "r", encoding="utf-8") as file:
    
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()
