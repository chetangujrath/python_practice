num1=float(input("Enter num 1 :"))
num2=float(input("Enter num 2 :"))
opr = input("enter oprator :")


if opr == "+":
    output=num1+num2

if opr == "-":
    output=num1-num2

if opr == "*":
    output=num1*num2

if opr == "%":
    output=num1/num2

print("your calculatiion is :", output)   

if num1 < 3:
    print ("num1 is less than 3")
elif num1 == 3:
    print("num1 is equal to 3")
else:
    print ("num1 is greter than 3")
