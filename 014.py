#사용자로부터 값 받기 활용 문항
letter = input("enter :")
if letter.isdigit():
    print("숫자")
elif letter.isalpha():
    print("영어")

#선생님 답안
s = input("Enter: ")
if s.isalpha():
    print("문자입니다.")
elif s.isnumeric():
    print("숫자입니다.")
else:
    print("??")
