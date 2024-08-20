import tkinter as tk
from tkinter import messagebox

def save_diary():
    diary_text = text.get("1.0", "end-1c")  # 텍스트 위젯 내용 가져오기
    if diary_text.strip():  # 내용이 있는 경우에만 저장
        with open("diary.txt", "w") as file:
            file.write(diary_text)
        messagebox.showinfo("저장 완료", "일기가 저장되었습니다.")
    else:
        messagebox.showwarning("경고", "일기 내용을 입력하세요.")

def load_diary():
    try:
        with open("diary.txt", "r") as file:
            diary_text = file.read()
        text.delete("1.0", "end")  # 텍스트 위젯 내용 초기화
        text.insert("1.0", diary_text)  # 저장된 일기 불러오기
    except FileNotFoundError:
        messagebox.showwarning("경고", "저장된 일기가 없습니다.")

# tkinter GUI 생성
root = tk.Tk()
root.title("일기장 애플리케이션")

text = tk.Text(root, wrap=tk.WORD)
text.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

save_button = tk.Button(root, text="저장", command=save_diary)
save_button.pack(padx=10, pady=5)

load_button = tk.Button(root, text="불러오기", command=load_diary)
load_button.pack(padx=10, pady=5)

quit_button = tk.Button(root, text="종료", command=root.quit)
quit_button.pack(padx=10, pady=5)

root.mainloop()
