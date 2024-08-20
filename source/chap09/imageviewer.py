import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("이미지 뷰어")

        # 이미지 뷰어 창 크기
        self.width = 600
        self.height = 400

        # 이미지 라벨 초기화
        self.label = tk.Label(root)
        self.label.pack(expand="true", fill="both")

        # 메뉴 생성
        menubar = tk.Menu(root)
        root.config(menu=menubar)

        # 파일 메뉴
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="파일", menu=file_menu)
        file_menu.add_command(label="열기", command=self.open_image)
        file_menu.add_command(label="닫기", command=self.close_image)
        file_menu.add_separator()
        file_menu.add_command(label="종료", command=root.quit)

        # 이미지 초기화
        self.image = None
        self.photo = None

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("이미지 파일", "*.jpg *.jpeg *.png *.gif *.bmp")])
        if file_path:
            self.image = Image.open(file_path)
            self.photo = ImageTk.PhotoImage(self.image)
            self.label.config(image=self.photo)
            self.root.geometry(f"{self.width}x{self.height}")

    def close_image(self):
        self.image = None
        self.photo = None
        self.label.config(image=None)
        self.root.geometry("")  # 창 크기 초기화

root = tk.Tk()
app = ImageViewer(root)
root.mainloop()
