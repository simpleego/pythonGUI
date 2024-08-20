import tkinter as tk
from tkinter import filedialog, messagebox
import os

def select_directory():
    directory_path = filedialog.askdirectory()  # 디렉토리 선택 대화상자 열기
    if directory_path:
        directory_var.set(directory_path)
        update_file_list(directory_path)

def update_file_list(directory):
    file_listbox.delete(0, tk.END)  # 리스트 박스 초기화
    try:
        files = os.listdir(directory)
        for file in files:
            file_listbox.insert(tk.END, file)
    except OSError as e:
        messagebox.showerror("오류", f"디렉토리를 읽을 수 없습니다: {str(e)}")

def delete_selected_file():
    selected_file = file_listbox.get(tk.ACTIVE)  # 선택된 파일 가져오기
    if selected_file:
        directory = directory_var.get()
        file_path = os.path.join(directory, selected_file)
        try:
            os.remove(file_path)
            update_file_list(directory)
            messagebox.showinfo("성공", f"{selected_file} 파일이 삭제되었습니다.")
        except OSError as e:
            messagebox.showerror("오류", f"파일을 삭제할 수 없습니다: {str(e)}")

# tkinter GUI 생성
root = tk.Tk()
root.title("파일 탐색 및 삭제 프로그램")

directory_var = tk.StringVar()

select_button = tk.Button(root, text="디렉토리 선택", command=select_directory)
select_button.pack()

selected_directory_label = tk.Label(root, textvariable=directory_var)
selected_directory_label.pack()

file_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
file_listbox.pack()

delete_button = tk.Button(root, text="선택한 파일 삭제", command=delete_selected_file)
delete_button.pack()

root.mainloop()
