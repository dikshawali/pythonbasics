#using map function

lst1=['1', '2', '3', '7']

#suppose I have a list and I want to apply function on each element of the list. What is the possible way to achieve this?

# for i in range(len(lst1)):
#     lst1[i]=int(lst1[i])

# for i in lst1:
#     print(type(i))

#but this method is quite long and we do require a shorter method than this


lst1=list(map(int, lst1))

for i in lst1:
    print(type(i))

#letus use user defined function

def adds_five(num):
    return num+5

lst1=list(map(adds_five, lst1))
print(lst1)

#using lambda function

lst1=list(map(lambda x: x*x, lst1))
print(lst1)

#prints boolean if number is greater than 50

lst1=list(map(lambda x: x>50, lst1))
print(lst1)

#letus learn filter function now

lst1=[1,2,3,4,5]

lst1=list(filter(lambda x: x%2==1, lst1))

print(lst1)


