data_dic = {}
with open('data.txt', 'r') as handle:
    for line in handle:
        line_s = line.strip().split()
        data_dic[line_s[0]] = line_s[1]

print(data_dic)
gene_k = []
gene_dic = {}
with open('gene.txt', 'r') as handle:
    for line in handle:
        gene_k.append(line.strip().split())
#print(gene_k)
a = ''
for i in gene_k:
    if i in data_dic.keys():
        a += i+'\t'+data_dic[i]
    a += i+'\t'+'NA'
print(a)
