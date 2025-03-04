import tkinter as tk

def show_text():
    # 입력된 텍스트를 가져와서 레이블에 표시
    input_text = entry.get()
    label.config(text=input_text)

root = tk.Tk()
root.geometry("300x200")

entry = tk.Entry(root)
entry.pack()

# 버튼을 클릭하면 show_text 함수를 호출
button = tk.Button(root, text="입력", command=show_text)
button.pack()

label = tk.Label(root, text="여기에 입력한 텍스트가 표시됩니다.")
label.pack()

root.mainloop()
