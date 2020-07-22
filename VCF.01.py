cnt = 0
with open('070.vcf', 'r') as handle:
    for line in handle:
        if line.sartswith('##'):
            continue
        if line.startswith('#'):
            header = line.strip().split('\t')
            filt_idx = header.index('FILTER')

       splitted = line.strip().split('\t')
       if splitted[filt_idx] == 'PASS':
           cnt += 1

#print(cnt)
