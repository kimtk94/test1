#16 파일 읽기
#내 답안
f = open("read_sample.txt", "r")
r = f.read()
print(r)
f.close()

#선생님 답안
with open("read_sample.txt", "r") as handle:
    for line in handle:
        #'>'가 나오는 줄은 생략
        if line.startswith(">"):
            continue

        print(line.strip())

