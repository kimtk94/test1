
#sys.argv 사용하기

import sys

f = sys.argv[1]

with open(f, 'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        print(line.strip())

