import re

#Check if the string starts with "The" and ends with "Spain":

# txt = '#122'
# x = re.findall(r'\#+[A-F]|[0-9]|[a-z]+[A-F]|[0-9]|[a-z]+[A-F]|[0-9]|[a-z]+[A-F]|[0-9]|[a-z]+[A-F]|[0-9]|[a-z]', txt)
# print(x)

# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")

# txt='12233'
# x=re.findall(r'(\w)\1', txt)
# print(x)

import re
answer=-1
txt='rabcdeefgyYhFjkIoomnpOeorteeeeet'
regex_exp=r'([b-d]|[f-h]|[j-n]|[p-t]|[v-z]|[B-D]|[F-H]|[J-N]|[P-T]|[V-Z]){1}([a|e|i|o|u|A|E|I|O|U]){2,}([b-d]|[f-h]|[j-n]|[p-t]|[v-z]|[B-D]|[F-H]|[J-N]|[P-T]|[V-Z]){1}'
answer=[]
while re.search(regex_exp, txt):
    match = re.search(regex_exp, txt)
    # print('Start Index:', match.start())
    # print('End Index:', match.end())
    answer.append(txt[match.start():match.end()])
    print(txt[match.start()+1:match.end()-1])
    txt=txt.replace(txt[match.start():match.end()],'',1)
    # break
print(answer)
 


# s=re.findall(regex_exp, txt)
# print(s)


