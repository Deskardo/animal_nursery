from animal_registry.models.pets import Dog, Cat, Hamster
from animal_registry.models.pack_animal import Horse, Camel, Donkey
from animal_registry.models.animals import Animal
import animal_registry.presenters.test_function as t
import animal_registry.presenters.add_animal_base_methods as add_animal


class Methods:
    registry = []

    def __init__(self, view):
        self.view = view

    def add_animal(self):
        animals = {'dog': Dog, 'cat': Cat, 'hamster': Hamster, 'horse': Horse, 'camel': Camel, 'donkey': Donkey}

        name = add_animal.set_name()
        birth_date = add_animal.set_date()
        animal_type = add_animal.set_type()

        animal = animals[animal_type](name, birth_date)
        animal.pet_commands = animal.commands()
        self.registry.append(animal)
        print(f"{animal.type_of_animal} {animal.name} added successfully!")

    def list_commands(self):
        name = add_animal.set_name()
        animal_type = add_animal.set_type()

        for animal in self.registry:
            if animal.name == name and animal.type_of_animal == animal_type:
                print(animal.name, animal.birth_date, animal.pet_commands)

    def train_commands(self):
        name = add_animal.set_name()
        birth_date = add_animal.set_date()

        for animal in self.registry:
            if animal.name == name and animal.birth_date == birth_date:
                command = add_animal.set_command()
                animal.pet_commands.append(command)
                print(f"{command} added successfully!")

    def list_animals_by_birth_date(self):
        pattern = '%Y-%m-%d'
        for animal in sorted(self.registry, key=lambda x: t.datetime.strptime(x.birth_date, pattern)):
            print(animal.type_of_animal, animal.name, animal.birth_date, animal.pet_commands)
        pass

    def show_animal_count(self):
        print("Total count of animals:", Animal.count)
