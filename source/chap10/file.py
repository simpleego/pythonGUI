import tkinter as tk
from tkinter import filedialog
import os

class FileExplorer:
    def __init__(self, root):
        self.root = root
        self.root.title("파일 탐색기")

        self.current_directory = os.getcwd()  # 현재 작업 디렉토리
        self.file_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.file_listbox.pack(fill=tk.BOTH, expand=True)

        # 디렉토리 변경 버튼
        self.change_dir_button = tk.Button(root, text="디렉토리 변경", command=self.change_directory)
        self.change_dir_button.pack()

        # 파일 열기 버튼
        self.open_file_button = tk.Button(root, text="파일 열기", command=self.open_file)
        self.open_file_button.pack()

        # 현재 디렉토리 표시 레이블
        self.current_dir_label = tk.Label(root, text="현재 디렉토리: " + self.current_directory)
        self.current_dir_label.pack()

        self.update_file_list()

    def change_directory(self):
        new_directory = filedialog.askdirectory()
        if new_directory:
            self.current_directory = new_directory
            self.update_file_list()

    def open_file(self):
        selected_index = self.file_listbox.curselection()
        if selected_index:
            selected_file = self.file_listbox.get(selected_index[0])
            selected_path = os.path.join(self.current_directory, selected_file)
            os.system(f'start "" "{selected_path}"')

    def update_file_list(self):
        self.file_listbox.delete(0, tk.END)
        self.current_dir_label.config(text="현재 디렉토리: " + self.current_directory)
        files = os.listdir(self.current_directory)
        for file in files:
            self.file_listbox.insert(tk.END, file)

root = tk.Tk()
app = FileExplorer(root)
root.mainloop()
