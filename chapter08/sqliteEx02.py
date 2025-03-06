import sqlite3

try:
    # 데이터베이스 연결
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    # 테이블 생성
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        department TEXT NOT NULL,
                        salary INTEGER NOT NULL
                    )''')
    conn.commit()

    # 데이터 삽입 (사용자 입력)
    name = input("직원 이름을 입력하세요: ")
    department = input("부서를 입력하세요: ")
    salary = int(input("연봉을 입력하세요: "))

    cursor.execute("INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
                   (name, department, salary))
    conn.commit()

    # 데이터 조회
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    print("\n직원 목록:")
    for row in rows:
        print(row)

except sqlite3.Error as e:
    print(f"데이터베이스 오류 발생: {e}")

except ValueError:
    print("잘못된 입력! 연봉은 숫자로 입력해야 합니다.")

finally:
    if conn:
        conn.close()
