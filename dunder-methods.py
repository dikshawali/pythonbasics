class String_class:
    #magic command to initiate object

    def __init__(self, str1_arg):
        self.str1=str1_arg

    #command that prints our string whenever we try to print the location of the string
    def __repr__(self):
        return (f'The main content of the class is {self.str1}.')

    # this method overrides the addition
    def __add__(self, other):
        return (self.str1 + other.str1)

    def __str__(self):
        return f'This is a __str__ function and the variable in this class is {self.str1}'


s=String_class('hello')
o=String_class('hii')
print(s)
# print(s+o)