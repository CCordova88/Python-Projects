class Animal:
    name = 'Unknown'
    animalia = 'Unknown'
    diet = 'Unknown'
    extant = True

    def Description(self):
        x = Animal()
        msg = "\nName: {} \nAnimalia: {} \nDiet: {} \nExtant: {}".format(x.name,x.animalia,x.diet,x.extant)
        return msg
        

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

class Fish(Animal):
    name = 'Shark'
    animalia = 'Vertebrate'
    diet = 'Carnivore'
    extant = True
    respiration = 'Gills'
    habitat_type = 'Saltwater'
    
    def Description(self):
        f = Fish()
        msg = "\nName: {} \nAnimalia: {} \nDiet: {} \nExtant: {} \nRespiration: {} \nHabitat Type: {}".format(f.name,f.animalia,f.diet,f.extant,f.respiration,f.habitat_type)
        return msg




if __name__ == "__main__":
    print(Mammal().Description())

    print(Fish().Description())
