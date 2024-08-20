import copy

original_list = [1, [2, 3], 4]
shallow_copy = copy.copy(original_list)

print(shallow_copy)	# 출력: [1, [2, 3], 4] 
# 얕은 복사이므로 하위 리스트는 같은 객체를 참조
print(original_list[1] is shallow_copy[1])	# 출력: True
