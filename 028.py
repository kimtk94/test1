#28 문자열 바꾸기

seq1 = 'ATGTTATAG'
seq1_r = seq1.replace('A', 't')
seq1_r = seq1_r.replace('T', 'a')
seq1_r = seq1_r.replace('C', 'g')
seq1_r = seq1_r.replace('G', 'c').upper()

print(seq1_r)


