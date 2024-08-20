from tkinter import *
from tkinter.messagebox import showinfo
root = Tk()
root.geometry("300x200")
root.title("Checkbox Demo")
# 체크박스의 상태를 저장하는 변수
agree = StringVar()
# 초기 상태를 "비동의"로 설정
agree.set("비동의")
# 체크박스 클릭 시 실행될 함수
def event_proc() :
    showinfo(title="결과", message=agree.get())
# 체크박스 생성 및 배치
Checkbutton(root,
    text="동의합니다.",
    command=event_proc,
    variable=agree,
    onvalue="동의",
    offvalue="비동의").pack()
root.mainloop()
