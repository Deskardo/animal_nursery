from animal_registry.models.animals import Animal


class PackAnimal(Animal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)


class Horse(PackAnimal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
        self.type_of_animal = "horse"
        self.pet_commands = []

    def sound(self):
        return "Neigh!"

    def commands(self):
        return ["Gallop", "Jump obstacles", "Carry load"]


class Camel(PackAnimal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
        self.type_of_animal = "camel"
        self.pet_commands = []

    def sound(self):
        return "Grunt!"

    def commands(self):
        return ["Walk long distances", "Carry load", "Endure heat"]


class Donkey(PackAnimal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
        self.type_of_animal = "donkey"
        self.pet_commands = []

    def sound(self):
        return "Hee-haw!"

    def commands(self):
        return ["Carry load", "Endure heat", "Bray"]
