import sys

ret = ''
def read_txt(file_name : str) -> str:
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith('>'):
                continue
            else:
                ret += line.strip()

print(ret)
