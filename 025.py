#25 문자열 n씩 건너뛰며 출력하기

seq1 = "ATGTTATAG"
Ans = []
for i in range(0,len(seq1), 3):
    Ans.append(seq1[i])

print(Ans)


#강사님 답안
for i in range(0, len(seq1),3):
    print(i, seq1[i])
