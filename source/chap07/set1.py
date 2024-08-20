numbers = {2, 1, 3}
print(numbers)
print(len(numbers))


fruits = { "Apple", "Banana", "Pineapple" } 
mySet = { 1.0, 2.0, "Hello World", (1, 2, 3) }


cities = { "Paris", "Seoul", "London", "Berlin", "Paris", "Seoul" }
print(cities)

numbers = set()
numbers = {2, 1, 3}
if 2 in numbers:
	print("집합 안에 2가 있습니다.")


numbers = {2, 1, 3}
for x in numbers:
	print(x, end=" ")
	
for x in sorted(numbers):
	print(x, end=" ")

# numbers = {1, 2, [3, 4, 5]}

set([1, 2, 3, 1, 2, 3])
set("abcdefa")

for char in set("banana"):
	print(char)
