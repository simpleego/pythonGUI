from tkinter import *

root = Tk()
photo = PhotoImage(file="wl.gif")
w = Label(root, image=photo, justify="left").pack(side="right")
message= """삶이 그대를 속일지라도
슬퍼하거나 노하지 말라 !
우울한 날들을 견디면 : 믿으라,
기쁨의 날이 오리니.
마음은 미래에 사는 것
현재는 슬픈 것:
모든 것은 순간적인 것, 지나가는 것이니
그리고 지나가는 것은 훗날 소중하게 되리니.
"""
w2 = Label(root, 
           padx = 10, 
           text=message).pack(side="left")
root.mainloop()
