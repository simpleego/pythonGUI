from tkinter import *

def submit():
    name = entry_name.get()
    age = entry_age.get()
    print("이름:", name)
    print("나이:", age)

root = Tk()
root.geometry("300x200")

Label(root, text="이름:").pack()      # 레이블 참조 변수는 필요하지 않다. 

entry_name = Entry(root)
entry_name.pack()

Label(root, text="나이:").pack()      # 레이블 참조 변수는 필요하지 않다. 
entry_age = Entry(root)

entry_age.pack()
button_submit = Button(root, text="제출", command=submit)
button_submit.pack()

root.mainloop()
