from animal_registry.models.pets import Pet
from animal_registry.models.pack_animal import PackAnimal
from animal_registry.models.animals import Animal


class MenuPresenter:
    def __init__(self, view):
        self.view = view

    def handle_choice(self, choice):
        if choice == "1":
            self.add_animal()
        elif choice == "2":
            self.list_commands()
        elif choice == "3":
            self.train_commands()
        elif choice == "4":
            self.list_animals_by_birth_date()
        elif choice == "5":
            self.show_animal_count()

    def add_animal(self):
        name = input("Enter the name of the animal: ")
        birth_date = input("Enter the birth date of the animal: ")
        animal_type = input("Enter the type of animal (dog, cat, hamster, horse, camel, donkey): ")

        if animal_type == "dog" or animal_type == "cat":
            animal = Pet(name, birth_date)
        else:
            animal = PackAnimal(name, birth_date)

        print("Animal added successfully!")

    def list_commands(self):
        name = input("Enter the name of the animal: ")
        # Find the animal in the registry
        # Call the commands() method on the animal and print the result

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
