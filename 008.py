#8 while : 5!=?
#내 답안
i = 0
Ans = 1

while i < 5:
    i+=1
    Ans *= i

print(Ans)


#선생님 답안
n = 5
total = 1

while n > 0:# condition
    total *= n
    n-= 1 # 탈출

print(total)
