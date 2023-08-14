# s='abcdef'

# for i in range(len(s)):
#     print(s[:i]+s[i+1:])
# n=3
# print(list(i for i in range(1,n+1)))

lst=[1,2,3,4,5]
dict1={}

if ','.join(list(map(str, lst))) not in dict1.keys():
    print('element not present')
    dict1[','.join(list(map(str, lst)))]=0

print(dict1)