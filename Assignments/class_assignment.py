class Animal
    name = 'Unknown'
    animalia = 'Unknown'
    diet = 'Unknown'
    extant = True

    def Description(self):
        msg = "Name: {} Animalia: {} Diet: {} Extant: {}"
        return msg
        

class Mammal(Animal)
    name = 'Tiger'
    animalia = 'Vertebrate'
    diet = 'Carnivore'
    extant = True
    locomotion = 'Quadrupedal'
    habitat = 'Jungle'

    def Description(self):
        msg = "Name: {} Animalia: {} Diet: {} Extant: {} Locomotion: {} Habitat: {}"
        return msg

class Fish(Animal)
    name = 'Shark'
    animalia = 'Vertebrate'
    diet = 'Carnivore'
    extant = True
    respiration = 'Gills'
    habitat_type = 'Saltwater'
    
    def Description(self):
        msg = "Name: {} Animalia: {} Diet: {} Extant: {} Respiration: {} Habitat Type: {}"
        return msg
