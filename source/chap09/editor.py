import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("텍스트 에디터")

        # 텍스트 위젯 생성
        self.text = tk.Text(root)
        self.text.pack(fill=tk.BOTH, expand=True)

        # 메뉴 생성
        menubar = tk.Menu(root)
        root.config(menu=menubar)

        # 파일 메뉴
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="파일", menu=file_menu)
        file_menu.add_command(label="열기", command=self.open_file)
        file_menu.add_command(label="저장", command=self.save_file)

        file_menu.add_command(label="다른 이름으로 저장", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="종료", command=root.quit)

        # 편집 메뉴
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="편집", menu=edit_menu)
        edit_menu.add_command(label="실행 취소", command=self.undo)
        edit_menu.add_command(label="다시 실행", command=self.redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="복사", command=self.copy)
        edit_menu.add_command(label="잘라내기", command=self.cut)
        edit_menu.add_command(label="붙여넣기", command=self.paste)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("텍스트 파일", "*.txt"), ("모든 파일", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                self.text.delete("1.0", tk.END)
                self.text.insert(tk.END, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("텍스트 파일", "*.txt"), ("모든 파일", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text.get("1.0", tk.END))

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("텍스트 파일", "*.txt"), ("모든 파일", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text.get("1.0", tk.END))

    def undo(self):
        try:
            self.text.edit_undo()
        except tk.TclError:
            pass

    def redo(self):
        try:
            self.text.edit_redo()
        except tk.TclError:
            pass

    def copy(self):
        self.text.clipboard_clear()
        text = self.text.get(tk.SEL_FIRST, tk.SEL_LAST)
        self.text.clipboard_append(text)

    def cut(self):
        self.copy()
        self.text.delete(tk.SEL_FIRST, tk.SEL_LAST)

    def paste(self):
        text = self.text.selection_get(selection="CLIPBOARD")
        self.text.insert(tk.INSERT, text)

root = tk.Tk()
app = TextEditor(root)
root.mainloop()
