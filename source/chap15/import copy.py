import copy

original_list = [[1, 2, 3], [4, 5, 6]]
deep_copied_list = copy.deepcopy(original_list)

# 객체 및 내부 객체 모두가 복사됨
print(deep_copied_list[0] is original_list[0])  # False
