import sys
length = 0

with open('077.bed', 'r') as handle:
    for line in handle:
        point = line.replace('\t', ' ').split()
        length += int(point[2]) - int(point[1])

print(length)
    

#선생님 답안
total = 0
with open('077.bed', 'r') as handle:
    for line in handle:
        splitted = line.strip().spplit()
        start = int(splitted[1])
        end = int(splitted[2])
        total += start - end

print(total)
