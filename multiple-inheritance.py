class Personality:
    
        itsname='Shreya'
        _itsage='33'
        __itsnationality='indian'

    def print_personality(self):
        return f"His/Her name is {self.itsname}. His/Her age is {self.itsage}. His/Her nationality is {self.itsnationality}."

class Family:
    def __init__(self, name, mother, father):
        self.name=name
        self.mother=mother
        self.father=father

    def print_family(self):
        return f"Father of {self.name} is {self.father} and mother is {self.mother}"

class singer_personality(Personality, Family):
    def print_singer_details(self):
        return f'{Personality.itsname} is a singer of {Personality.itsage} years. He/She is from {Personality.itsnationality}. His/Her family consists'+\
            #    f' of mother - {self.mother} and father - {self.father} and brother - {self.brother}'
    

shreya=singer_personality()




        