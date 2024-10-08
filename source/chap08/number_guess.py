from tkinter import *
import random

answer = random.randint(1,100)

def guessing():
	guess = int(guessField.get())

	if guess > answer:
		msg = "높음!"
	elif guess < answer:
		msg = "낮음!"
	else:
		msg = "정답!"
		
	resultLabel["text"] = msg
	guessField.delete(0, 5)

def reset():
	global answer
	answer = random.randint(1,100)
	resultLabel["text"] = "다시 한번 하세요!"

root = Tk()
root.configure(bg="white")
root.title("숫자를 맞춰보세요!")
root.geometry("500x80")

titleLabel = Label(root, text="숫자 게임에 오신 것을 환영합니다!", bg="white")
titleLabel.pack()

guessField = Entry(root)
guessField.pack(side="left")
tryButton = Button(root, text="시도", fg="green", bg="white", command=guessing )
tryButton.pack(side="left")

resetButton = Button(root, text="초기화", fg="red", bg="white", command=reset)
resetButton.pack(side="left")
resultLabel = Label(root, text="1부터 100사이의 숫자를 입력하시오.", bg="white") 
resultLabel.pack(side="left")

root.mainloop()
