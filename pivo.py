def pivo(self:int) -> int:
    self.pivo = 0
    cnt = 0
    List = []
    if cnt == 0:
        List.append(0)
    if cnt == 1:
        List.append(1)
    if cnt >= 2:
        n = List[n-1] + List[n-2]
        List.append
    cnt += 1
    print(List[n])

#선생님 답안
import sys
def fib(n: int) ->int:
    if n== 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1) #함수를 다시 대입! -> 재귀함수

n = lnt(sys.argv[1])

print(fib(n))
