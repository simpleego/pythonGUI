class Counter:
    def __init__(self,  initValue=0) :
        self.count = initValue
    def reset(self) :
        self.count = 0
    def increment(self):
        self.count += 1
    def get(self):
        return self.count

a = Counter(100)   # 카운터의 초기값은 100이 된다. 
b = Counter()       # 카운터의 초기값은 0이 된다. 
