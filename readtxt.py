import json
import sys

#def read_csv(file_name: str) -> str:
#    ret = []
#    return ret
#with open(file_name, 'r') as handle:
#    for line in handle:
#        ret_ine.split(',')
#        ret[id] = line.
#if __name__ = '__main__'
#    if len(sys.argv) != 2:
#        print("#usage: python {sys.argv.[0]} [txt])
#        sys.exit()")


#선생님 답안
def read_txt(file_name: str) -> str:
    ret = ''
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith('>'):
                continue
            ret += line.strip()
    return ret

def read_csv(file_name: str) -> str:
    ret = []
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split(",")
                continue
            splitted = line.strip().split(",")
            d = dict(zip(header, splitted))
            ret.append(d)
    return ret

def read_tsv(file_name: str) -> list:
    ret = []
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split("\t")
                continue
            splitted = line.strip().split("\t")
            d = dict(zip(header, splitted))
            ret.append(d)
    return ret

def to_json(l: list, file_name: str) -> None:
    with open(file_name, 'w') as handle:
        json.dump(l, handle, indent=4)

def read_json(file_name: str) -> list:
    with open(file_name, 'r') as handle:
        l = json.load(handle)
    return l

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("#usage: python {sys.argv.[0]} [txt]")
        sys.exit()

    file_name = sys.argv[1]
    #ret = read_csv(file_name)
    ret = read_tsv(file_name)
    to_json(ret, "result.json")
   
