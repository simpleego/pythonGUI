import random
print(random.randint(1, 6))
print(random.randint(1, 6))
print(random.random()*100)

myList = [ "red", "green", "blue" ]
print(random.choice(myList))

myList = [ [x] for x in range(10) ]
random.shuffle(myList)
print(myList)
