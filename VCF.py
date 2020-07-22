import sys
cnt = 0
dic_vcf = {}
cnt_pass = 0
with open('070.vcf', 'r') as handle:
    for line in handle:
        if line.startswith('##'):
            continue
        elif line.startswith('#'):
            header = line.strip().split()
        else:
            chr_n = line.strip().split()
            cnt += 1
            dic_vcf = dict(zip(header, chr_n))
            if dic_vcf['FILTER'] == 'PASS':
                cnt_pass += 1
                

#print(cnt)
#print(dic_vcf)
print(cnt_pass)
