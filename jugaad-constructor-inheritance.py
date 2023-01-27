class Student:
    def __init__(self, name):
        self.name=name

    def printstudents(self):
        print(f'The name of student is {self.name}')

class Interns(Student):
    def __init__(self, speciality):
        self.name=name
        self.speciality=speciality

    def printinterns(self):
        print(f'The name of the intern is {self.name} and his/her speciality is {self.speciality}')


diksha=Interns('Diksha', 'Data Engineering')
diksha.printinterns()
diksha.printstudents()

