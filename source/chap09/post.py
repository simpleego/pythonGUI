class Post:
    count = 0  			# 클래스 변수
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content
        Post.count += 1  		# 클래스 변수 업데이트

    def display_info(self):
        print("제목:", self.title)
        print("작성자:", self.author)
        print("내용:")
        print(self.content)
        print()

post1 = Post("첫 번째 게시글", "홍길동", "안녕하세요. 첫 번째 게시글입니다.")
post2 = Post("두 번째 게시글", "이순신", "안녕하세요. 두 번째 게시글입니다.")

post1.display_info()
post2.display_info()

print("총 게시글 개수:", Post.count)		# 게시글 총 개수 출력
