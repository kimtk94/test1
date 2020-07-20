#5 if-elif-else
num1 = 21
if num1 % 3 == 0 and num1 % 7 ==0:
    print(num1,"는 3과 7의 배수")
elif num1 % 3 == 0:
    print(num1, "는 3의 배수")
elif num1 % 7 == 0:
    print(num1,"는 7의 배수")
else:
    print("3, 7의 배수가 아님")
