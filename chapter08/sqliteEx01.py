import sqlite3


conn = sqlite3.connect("example.db")  
cursor = conn.cursor()  

# 2️⃣ 테이블 생성
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    grade TEXT NOT NULL
                )''')
conn.commit()

# 3️⃣ 데이터 삽입
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("이쁜이", 18, "A"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("철수", 20, "B"))
conn.commit()

# 4️⃣ 데이터 조회
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("학생 목록:")
for row in rows:
    print(row)

# 5️⃣ 데이터 수정
cursor.execute("UPDATE students SET grade = ? WHERE name = ?", ("A+", "철수"))
conn.commit()

# 6️⃣ 데이터 삭제
cursor.execute("DELETE FROM students WHERE name = ?", ("이쁜이",))
conn.commit()

# 최종 조회 결과
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("\n최종 학생 목록:")
for row in rows:
    print(row)

# 7️⃣ 연결 종료
conn.close()
