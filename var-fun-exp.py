# var1=2
# var2=var1

# print(var1, var2)
# var2=3
# print(var1, var2)
# var1=4
# print(var1, var2)

def executor(func):
    func('hello hii')
# 
# print(executor())

executor2=executor

print(executor2())