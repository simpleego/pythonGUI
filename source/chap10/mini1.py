import tkinter as tk
from tkinter import messagebox

def calculate_statistics():
    input_text = entry.get()  # 사용자로부터 숫자 리스트 입력 받음
    try:
        numbers = list(map(int, input_text.split(',')))  # 쉼표로 구분된 숫자를 리스트로 변환
        if numbers:
            total = sum(numbers)
            count = len(numbers)
            average = total / count
            maximum = max(numbers)
            minimum = min(numbers)

            result_message = f"총합: {total}\n개수: {count}\n평균: {average:.2f}\n최댓값: {maximum}\n최솟값: {minimum}"
            messagebox.showinfo("통계 정보", result_message)
        else:
            messagebox.showwarning("경고", "숫자를 입력하세요.")
    except ValueError:
        messagebox.showerror("오류", "올바른 숫자 형식이 아닙니다.")

root = tk.Tk()
root.title("숫자 통계 계산기")

label = tk.Label(root, text="숫자를 쉼표로 구분하여 입력하세요:")
label.pack()

entry = tk.Entry(root)
entry.pack()

calculate_button = tk.Button(root, text="계산", command=calculate_statistics)
calculate_button.pack()

quit_button = tk.Button(root, text="종료", command=root.quit)
quit_button.pack()

root.mainloop()
