colors = ("red", "green", "blue")
print(colors)

numbers = (1, 2, 3, 4, 5 )
print(numbers)

t = (1, 2, 'hello!')
print(t)

t = ()
t = (10, )

t = tuple([1, 2, 3, 4, 5])
t = (1, 2, 'hello!')
u = t, (1, 2, 3, 4, 5)
print(u)

numbers = (1, 2, 3, 4, 5)
print(len(numbers))

t1 = (1, 2, 3, 4, 5)
# t1[0] = 100

numbers = (1, 2, 3, 4, 5)
colors = ('red', 'green', 'blue')
t = numbers + colors # 리스트와 같이 + 연산자를 사용하여 합병할 수 있다.
print(t)
