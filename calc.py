num1=float(input("Enter The First No.:"))
num2=float(input("Enter The Second No.:"))
op=input("Enter Operator[+,-,*,/,%]:")
result=0
if op=='+':
    result=num1+num2
elif op=='-':
    result=num1-num2
elif op=='*':
    result=num1*num2
elif op=='/':
    result=num1/num2
elif op=='%':
    result=num1%num2
else:
    print("Invalid Operator!!")
print(num1,op,num2,'=',result)'''
