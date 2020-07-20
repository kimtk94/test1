#10 함수 - 함수에 값 전달
#내 답안 = 선생님 답안
def mySum(num1: int, num2: int) -> None:
    print(f"{num1} +dd {num2} = {num1+num2}")

res1 = mySum(2, 3)
res2 = mySum(5, 7)
res3 = mySum(10, 15)
#추가 내용(함수에서 return이 없을때 함수를 print하면 None이 나온다.
print(res1) # None
print(res2) # None
print(res3) # None
