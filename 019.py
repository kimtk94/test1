import sys

if len(sys.argv) !=2:
    print("#usage: python {sys.argv[0]} [num]")
    sys.exit()
try:
    num = int(sys.argv[1])
except ValueError:
    print("imput not valid")
    sys.exit() #오류가 났을 때 멈춰야 하므로
try:
    print(10 / num) # 위에 있는 try에 합쳐도 됨
except ZeroDivisionError:
    print("0으로는 못나눠요.")
## 예시

#try:
#    num = int(sys.argv[1])
#    print(10 / num)
#except ValueError:
#    print("imput not valid")
#... ...

