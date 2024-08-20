import tkinter as tk
from tkinter import messagebox
import pickle

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do 리스트")

        self.todo_list = []
        self.load_tasks()  # 앱 실행 시 저장된 할 일 목록 불러오기

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.listbox = tk.Listbox(root)
        self.listbox.pack()

        add_button = tk.Button(root, text="추가", command=self.add_task)
        add_button.pack()

        complete_button = tk.Button(root, text="완료", command=self.complete_task)
        complete_button.pack()

        save_button = tk.Button(root, text="저장", command=self.save_tasks)
        save_button.pack()

    def add_task(self):
        task = self.entry.get()
        if task:
            self.todo_list.append({"task": task, "completed": False})
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)

    def complete_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.todo_list[index]["completed"] = True
            self.listbox.itemconfig(index, {'bg': 'light green'})

    def save_tasks(self):
        with open("tasks.pkl", "wb") as file:
            pickle.dump(self.todo_list, file)
        messagebox.showinfo("저장", "할 일 목록이 저장되었습니다.")

    def load_tasks(self):
        try:
            with open("tasks.pkl", "rb") as file:
                self.todo_list = pickle.load(file)
                for task in self.todo_list:
                    self.listbox.insert(tk.END, task["task"])
        except FileNotFoundError:
            self.todo_list = []

root = tk.Tk()
app = TodoApp(root)
root.mainloop()
