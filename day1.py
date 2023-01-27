#today I am making faulty calculator 

oper=str(input('please enter the operator'))
num1=int(input('please enter the first number'))
num2=int(input('please enter the second number'))

solution=0

if(num1==45 and num2==3 and oper=='*'):
    solution=555

elif(num1==56 and num2==9 and oper=='+'):
    solution=77

elif(num1==56 and num2==6 and oper=='/'):
    solution=4

else:
    if(oper=='*'):
        solution=num1*num2
    elif(oper=='+'):
        solution=num1+num2
    elif(oper=='-'):
        solution=num1-num2
    elif(oper=='/'):
        solution=num1/num2

print('Our solution is '+str(solution))


        