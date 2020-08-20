




from abc import ABC, abstractmethod
class Animal(ABC):
    name = 'Unknown'
    animalia = 'Unknown'
    diet = 'Unknown'
    extant = True

    def Description(self):
        x = Animal()
        msg = "\nName: {} \nAnimalia: {} \nDiet: {} \nExtant: {}".format(x.name,x.animalia,x.diet,x.extant)
        return msg
    
    @abstractmethod
    def funFact(self):
        pass
        

class Mammal(Animal):
    name = 'Tiger'
    animalia = 'Vertebrate'
    diet = 'Carnivore'
    extant = True
    locomotion = 'Quadrupedal'
    habitat = 'Jungle'

    def Description(self):
        m = Mammal()
        msg = "\nName: {} \nAnimalia: {} \nDiet: {} \nExtant: {} \nLocomotion: {} \nHabitat: {}".format(m.name,m.animalia,m.diet,m.extant,m.locomotion,m.habitat,)
        return msg

    def funFact(self):
        m = Mammal()
        if m.name == 'Tiger':
            print("\nTigers have antiseptic saliva they can use to disinfect wounds.")

if __name__ == "__main__":
    m = Mammal()
    print(m.Description(),m.funFact())

    
