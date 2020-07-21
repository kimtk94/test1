f = '059.fasta'

A, C, G, T = 0, 0, 0, 0

with open(f, 'r') as handle:
    for line in handle:
        if line.startswith(">"):
            header = line.strip()
        else:
            seq = line.strip()
            A += seq.count('A')
            C += seq.count('C')
            G += seq.count('G')
            T += seq.count('T')
            
print(f"A: {A}")
print(f"C: {C}")
print(f"G: {G}")
print(f"T: {T}")
