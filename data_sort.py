dir_ = {}
data_k = []
data_v = []
with open('data.txt', 'r') as handle:
    for line in handle:
        line_s = line.split()
        data_k.append(line_s[0])
        data_v.append(line_s[1])

    dir_ =dict(zip(data_v, data_k))
    print(dir_)
    data_v.sort()
    print(data_v)

a = ''
for i in data_v:
    a += dir_[i]+'\t'+str(i)+'\n'
print(a)
