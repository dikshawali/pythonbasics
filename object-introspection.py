#object introsepection ka matlab hai koi bhi object uthana and uski full information lena ki wo kaha se aya hai bla 
#bla 

class Sample:
    pass

s=Sample()
# print(type(s), type('hello'))
print(id(s))
print(id('hii')) 
print(id('hii'))
print(id('hello'))
print(id('hii'))

# print(dir(s))
# print(dir('hii')) #dir=aap kya khilwaad kar sakte ho is string k sath

import inspect

print(inspect.getmembers(s))