import pandas as pd
gene = pd.read_csv('gene.txt', 'r', header=None)

print(gene[0])

data = pd.read_csv('data.txt', 'r', header=None)

print(data)


