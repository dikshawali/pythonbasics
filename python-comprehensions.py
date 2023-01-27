ls = []
for i in range (100):
    if i%3==0:
        ls.append(i)

# in one line
# list comprehension
ls=[ i for i in range(100) if i%3==0]
print(ls)


# dictionary comprehension

dict1={0:'item0', 1:'item1'}

dict1 = {i:f'item{i}' for i in range(100)}
dict2= {value:key for key, value in dict1.items()}
print(dict1)

# set comprehensions

# dresses={dress for dress in {'dress1', 'dress2'}}

set1={'value1', 'value2', 'value3', 'value1', 'value2'}

print(set1)

# generator comprehension

# tup1=(i for i in range(100))
# tup1=(1,2,3,4,5)
# print(tup1)
# print(type(tup1))

gen1=(i for i in range(10))
for item in gen1:
    print(item)
print('second:')
for item in gen1:
    print(item)
# generators works only once 