#선생님 답안

import sys
#1) for문 이용 -> 새로운 str 생성
def comp1(seq: str) -> str:
    comp = ""
    for s in seq:
        if s== "A"
            comp += "T"
        elif s== "C"
            comp += "G"
        elif s== "G"
            comp += "C"
        elif s== "T"
            comp += "A"
    return comp

#2) 사전사용 -> 서로 바꾸기 
def comp2(seq: str) -> str:
    d_comp = {"A":"T", "T":"A", "G":"C", "C":"G"}
    comp = ""
    for s in seq:
        comp += d_comp[s]
    return comp

#3) __name__ 사용하기
if __name__ == "__main__"
    if len(sys.argv) !=2:
        print(f"#usage: python {sys.argv[0]} [string]")
        sys.exit()
    seq = sys.argv[1]
    c1 = comp1(seq)
    c2 = comp2(seq)
    print(seq)
    print(c1)
    print(c2)
