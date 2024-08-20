contacts = {'Kim':'01012345678',  'Park':'01012345679', 'Lee':'01012345680' }
contacts['Choi'] = '01056781234'
print(contacts)


contacts = {'Kim':'01012345678',  'Park':'01012345679', 'Lee':'01012345680' }
print(contacts.pop("Kim"))
print(contacts)

contacts = {'Kim':'01012345678',  'Park':'01012345679', 'Lee':'01012345680' }
del contacts["Kim"]
print(contacts)

scores = { 'Korean': 80, 'Math': 90, 'English': 80}
for key in scores:
	print(key,  scores[key])


squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
print(1 in squares)
print(2 not in squares)

triples = { x: x*x*x for x in range(6) }
print(triples)

dic = { "bags": 1, "books": 5, "bottles": 4, "coins": 7, "cups": 2, "pens": 3 }
print(dic)

print(sorted(dic))
print(sorted(dic.values()))
print(sorted(dic, key=dic.__getitem__))
