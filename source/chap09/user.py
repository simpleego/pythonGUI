class User:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, User):     # User 객체이면
            return self.name == other.name  # 이름이 같은지 검사한다. 
        return False

user1 = User("Kim")
user2 = User("Lee")
user3 = User("Park")
user5 = User("Kim")

users = [user1, user2, user3]

print(user1 in users)    	# 출력: True
print(user5 in users)    	# 출력: True 
