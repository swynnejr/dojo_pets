class Ninja:
# implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
    def walk():
        pet.play() # <<<< I'm not sure about this
# feed() - feeds the ninja's pet invoking the pet eat() method
    def feed():
        pet.eat()  # <<<< I'm so confused
# bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe():
        pet.noise()  # <<<< This can't be right


class Pet:
# implement __init__( name , type , tricks ):
    def __init__(self, name, type, tricks):
        self.first_name = name
        self.type = type
        self.tricks = tricks
        self.energy = 50
        self.health = 50
# implement the following methods:
# sleep() - increases the pets energy by 25
    def sleep():
        self.energy += 25   # Why is SELF RED???
# eat() - increases the pet's energy by 5 & health by 10
    def eat():
        self.energy += 5
        self.health += 10
# play() - increases the pet's health by 5
    def play():
        self.health += 5
# noise() - prints out the pet's sound
    def noise():
        print("Beach Boys best selling album")



luke = Ninja("Luke", "Skywalker", "Blue Milk", "Oil", "R2D2")
R2D2 = Pet("R2D2", "Astromech Droid", "unlock blast doors")