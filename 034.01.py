l = [3, 1, 1, 2, 0, 0, 2, 3, 3]

import collections
list_C = dict(collections.Counter(l))
print(list_C)

#선생님 답안

d = {}

for elem in l:
    if elem in d:
        d[elem] += 1
    else:
        d[elem] = 1

print(d)
