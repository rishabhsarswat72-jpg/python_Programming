a=int(input("enter 1st number :"))
b=int(input('enter  2nd number:'))
operator=input("enter a operator(Addition,Subtraction,Multiplication,Division):")
if operator.title()=="Addition":
    print(f"addition is :{a+b}")
elif operator.title()=="Subtraction":
    print(f"substraction is:{a-b}")
elif operator.title()=="Multiplication":
    print(f"multiplication is :{a*b}")
elif operator.title()=="Division":
    if b==0:
        print("zero divisor error:division by zero")
    else:
        print(f"division is:{a/b}")
else:
    print("operator does not match")