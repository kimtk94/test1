#7 중첩 for 문
#내 답안
for i in range(2, 10, 2):
    print(i,"단")
    for j in range(1, 10):
        print(i * j)

#선생님 답안
for i in range(2, 10, 1):
    for j in range(1, 10, 1):
        if i % 2 == 0:
            print(f"{i} x {j} = {i*j}")#f스트링 사용
