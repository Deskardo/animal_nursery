from animal_registry.models.animals import Animal


class Pet(Animal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)


class Dog(Pet):
    def sound(self):
        return "Woof!"

    def commands(self):
        return ["Sit", "Stay", "Fetch"]


class Cat(Pet):
    def sound(self):
        return "Meow!"

    def commands(self):
        return ["Jump", "Pounce", "Scratch"]


class Hamster(Pet):
    def sound(self):
        return "Squeak!"

    def commands(self):
        return ["Run on wheel", "Hide food", "Climb"]
