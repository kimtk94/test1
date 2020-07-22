import sys


#선생님 답안

def mer(l1, l2, n):
    if n==1:
        return l2
    ltmp = []
    for s1 in l1:
        for s2 in l2:
            ltmp.append(s1 + s2)

    return mer(l1, ltmp, n-1)

l1 = ['A', 'T', 'C', 'G']
l2 = ['A', 'T', 'C', 'G']
n = int(sys.argv[1])

print(mer(l1, l2, n))
