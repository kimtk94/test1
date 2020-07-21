import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]}[fasta]")
    sys.exit()

f = sys.argv[1]
d = {}

with open(f, 'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        for s in line.strip():
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
total = 0
for k,v in d.items(): # value = 각 개수
    total += v

with open("resullt.txt", 'w') as handle:
    handle.write(f"A: {d['A']}\n") #d디렉터리에서 A의 value를 찾는다. -> A의 개수이다.
    handle.write(f"C: {d['C']}\n") # C의 개수
    handle.write(f"G: {d['G']}\n")
    handle.write(f"T: {d['T']}\n")
