class Student:
    
    def __init__(self, name1, rno1, subj1):
        self.name=name1
        self.rno=rno1
        self.subj=subj1

    @classmethod
    def constr(cls, str1):
        params = str1.split('-')
        return cls(params[0], params[1], params[2])

    @staticmethod
    def greetings():
        print('Good morning')


    
# diksha=Student('Diksha Wali', 149, 'Chemistry')
# ishani=Student(name1='Vishakha')

# print(ishani.name, ishani.rno, ishani.subj)

#cls method

diksha=Student.constr('diksha wali-122-cn')
print(diksha.name, diksha.rno, diksha.subj)
diksha.greetings()




