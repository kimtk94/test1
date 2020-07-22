cnt = 0
with open('070.vcf', 'r') as handle:
    for line in handle:
        if line.sartswith('##'):
            continue
        if line.startswith('#'):
            header = line.strip().split('\t')
            id_idx = header.index('ID')
            continue

        splitted = line.strip().split('\t')
        chrom = splitted[0]
        pos = splitted[1]
        id_ = splitted[2]
        ref = splitted[3]
        alt = splitted[4]
        if splitted[id_idx] == 'PASS':
           print(f"{chrom}-{pos}-{ref}-{alt}-{id_}")


