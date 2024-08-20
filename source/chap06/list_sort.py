a = [3, 2, 1, 5, 4]
a.sort()
print(a)

a = [3, 2, 1, 5, 4]
b = sorted(a)
print(b)

print(sorted("A picture is worth a thousand words.".split(), key=str.lower))
