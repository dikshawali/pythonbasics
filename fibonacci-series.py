count=input('Enter the limit of the series')

answer=[0,1]

if count==0:
    answer=[]
elif count==1:
    answer=[0]
elif count>=3:
    def fib_func(num1, num2, count):
        if count==0:
            return
        answer.append(num1+num2)
        fib_func(num2, num1+num2, count-1)

    fib_func(0, 1, count-2)
print(answer)
