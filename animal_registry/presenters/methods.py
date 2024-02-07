from animal_registry.models.pets import Dog, Cat, Hamster
from animal_registry.models.pack_animal import Horse, Camel, Donkey
from animal_registry.models.animals import Animal
import animal_registry.presenters.test_function as t
import animal_registry.presenters.add_animal_base_methods as add_animal


class Methods:
    registry = {}

    def __init__(self, view):
        self.view = view

    def add_animal(self):
        animals = {'dog': Dog, 'cat': Cat, 'hamster': Hamster, 'horse': Horse, 'camel': Camel, 'donkey': Donkey}

        name = add_animal.set_name()
        birth_date = add_animal.set_date()
        animal_type = add_animal.set_type()

        animal = animals[animal_type](name, birth_date)
        animal.pet_commands = animal.commands()
        self.registry[animal] = (animal.name, animal.type_of_animal, animal.birth_date, animal.pet_commands)
        print(f"{animal.type_of_animal} {animal.name} added successfully!")

    def list_commands(self):
        name = self.view.set_name()
        animal_type = self.view.set_type()

        # for animal in self.registry:
        #     if animal.name == name and animal.type_of_animal == animal_type:
        #         return

        return []

    def train_commands(self):
        name = input("Enter the name of the animal: ")
        # Find the animal in the registry
        # Prompt the user to enter a new command
        # Add the new command to the animal's list of commands

    def list_animals_by_birth_date(self):
        # Sort the animals in the registry by birth date
        # Print the sorted list of animals
        pass

    def show_animal_count(self):
        print("Total count of animals:", Animal.count)
