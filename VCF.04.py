import pandas as pd
from matplotlib import pyplot as plt

d = {'SNP':0, 'ins':0, 'del':0}
with open('070.vcf', 'r') as handle:
    for line in handle:
        if line.startswith('#'):
            continue

        splitted = line.strip().split('\t')
        ref = splitted[3]
        alts = splitted[4].split(",")
        for alt in alts:
            if len(ref) == len(alt):
                d['SNP'] += 1
            elif len(ref) > len(alt):
                d['del'] += 1
            elif len(ref) < len(alt):
                d['ins'] += 1

print(d)
df = pd.DataFrame([d])
print(df)
df.plot.bar()
plt.savefig("v.png")
