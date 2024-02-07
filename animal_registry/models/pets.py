from animal_registry.models.animals import Animal


class Pet(Animal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)


class Dog(Pet):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
        self.type_of_animal = "dog"
        self.pet_commands = []

    def sound(self):
        return "Woof!"

    def commands(self):
        return ["Sit", "Stay", "Fetch"]


class Cat(Pet):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
        self.type_of_animal = "cat"
        self.pet_commands = []

    def sound(self):
        return "Meow!"

    def commands(self):
        return ["Jump", "Pounce", "Scratch"]


class Hamster(Pet):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
        self.type_of_animal = "hamster"
        self.pet_commands = []

    def sound(self):
        return "Squeak!"

    def commands(self):
        return ["Run on wheel", "Hide food", "Climb"]
