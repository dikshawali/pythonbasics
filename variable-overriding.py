#a program to understand the flow of overriding variables in classes

class Parent1:
    var1='This is variable in parent class'
    print(var1)
    def __init__(self):
        self.var1='This is instance variable in parent constructor'
        print(self.var1)


class Child(Parent1):
    var1='This is a variable in child class'
    print(var1)
    def __init__(self):
        # super().__init__()
        var1='This is instance variable in child constructor'
        print(self.var1)
        super().__init__()

a=Child()
print(a.var1)
