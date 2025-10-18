def get_number(number):
    while True:
        operand=input("Enter an Number: ")
        try:
            operand=float(operand)
            return operand
            
        except Exception as e:
            print("Invalid",e)

operand1=get_number()
operand2=get_number()
sign=input("Enter Sign: ")
result=0

if sign=="+":
    result= operand1 + operand2
    print(result)
elif sign=="-":
    result= operand1 - operand2
    print(result)
elif sign=="*":
    result = operand1 * operand2
    print(result)
elif sign=="/":
    if operand2 != 0:
        result=operand1 / operand2
        print(result)
    else:
        print("division by zero not allowed") 
else:
    print("Invalid sign")
    print("quitting")   
    quit()