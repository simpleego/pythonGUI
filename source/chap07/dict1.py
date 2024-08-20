d = {1: 'apple',  2: 'banana'}

contacts = {'Kim':'01012345678',  'Park':'01012345679', 'Lee':'01012345680' }
print(contacts)

d = { }

contacts = {'Kim':'01012345678',  'Park':'01012345679', 'Lee':'01012345680' }

print(contacts['Kim'])
print(contacts.get('Kim'))

number = contacts.get("Choi", "010114")
print(number)

if "Kim" in contacts:
	print("키가 딕셔너리에 있음")
