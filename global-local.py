global_var=23

for i in range(5):
    local_var=66

def func1():
    local_var2=88

func1()
print(global_var, local_var, local_var2)