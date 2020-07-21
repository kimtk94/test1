
import sys

def read_csv(file_name: str) -> str:
    ret = []
    return ret
with open(file_name, 'r') as handle:
    for line in handle:
        ret_ine.split(',')
        ret[id] = line.
if __name__ = '__main__'
    if len(sys.argv) != 2:
        print("#usage: python {sys.argv.[0]} [txt])
        sys.exit()")


#선생님 답안
import sys

def read_csv(file_name: str) -> str:
    ret = []
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith("#")
                header = line.strip().split(",")
                continue
            splitted = line.strip().split(",")
            d = dict(zip(geader, splitted))
            ret.append(d)
    return ret

if __name__ = '__main__'
    if len(sys.argv) != 2:
        print("#usage: python {sys.argv.[0]} [txt])
        sys.exit()")

