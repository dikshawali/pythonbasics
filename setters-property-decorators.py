class Employee:
    def __init__(self, first, last):
        self.fname=first
        self.lname=last
        # self.email=f'{self.fname}.{self.lname}@gmail.com'

    @property
    def email(self):
        if self.fname == None or self.lname ==None:
            return "Can't create email id! sorry!"
        return f'{self.fname}.{self.lname}@gmail.com'

    @email.setter
    def email(self, str1):
        self.fname=str1.split('@')[0].split('.')[0]
        self.lname=str1.split('@')[0].split('.')[1]

    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None


d=Employee('Diksha', 'Wali')
s=Employee('Ishani', 'Wali')

print(d.email)
print(s.email)

d.email='this.that@gmail.com'
del d.email

print(d.email, d.fname, d.lname)




