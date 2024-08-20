import copy

original_list = [1, [2, 3], 4]
deep_copy = copy.deepcopy(original_list)

print(deep_copy)		# 출력: [1, [2, 3], 4]  
# 깊은 복사이므로 하위 리스트도 별개의 객체를 참조
print(original_list[1] is deep_copy[1])	# 출력: False
