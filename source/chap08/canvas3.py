from tkinter import *

root = Tk()

w = Canvas(root, width=300, height=200)
w.pack()

i = w.create_line(0, 0, 300, 200, fill="red")   # (1)
w.coords(i, 0, 0, 300, 100)         # 좌표를 변경한다. 
w.itemconfig(i, fill="blue")    # 색상을 변경한다. 

#w.delete(i)            # 삭제한다. 
#w.delete(ALL)          # 모든 항목을 삭제한다. 

root.mainloop()
