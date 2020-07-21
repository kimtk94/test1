# 리스트에서 가장 큰 값, 작은 값 구하기
list = [3, 1, 1, 2, 0, 0, 2, 3, 3]

max_val = list[0]
min_val = list[0]

for elem in list:
    if elem > max_val:
        max_val = elem
    elif elem < min_val:
        min_val = elem


print(f"max: {max_val}")
print(f"min: {min_val}")
