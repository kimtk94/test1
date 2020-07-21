import sys

def read_txt(file_name, 'r') -> str:
    ret = ''
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith(">"):
                continue
            ret += line.strip()
    return

def read_csv(file_name:str) -> list:
    ret = []
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split(",")
                continue
            splitted = line.strip().split(',')
            d = dict(zip(header, splitted))
            ret.append(d)
    return ret

if __name__ == '__main__':
    if len(sys.argv) !=2:
        print(f"#usage: python {sys.argv[0]} {txt}")
        sys.exit()

    file_name = sys.argv[1]
    txt = read_txt(file_name)
    print(txt)
    ret = read_csv(file_name)
    print(ret)
