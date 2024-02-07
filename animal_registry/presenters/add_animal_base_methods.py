from datetime import datetime

import animal_registry.presenters.test_function as t


def set_name():
    name = input("Enter the name of the animal format 'Name' minimal len is 3 characters: ").capitalize()
    while not t.is_correct_name(name):
        name = input("Your input is incorrect enter the correct Name format 'Name': ").capitalize()
    return name


def set_date():
    birth_date = input("Enter the birth date format 'YYYY-MM-DD': ")
    while not t.is_correct_date(birth_date):
        birth_date = input("Is incorrect date age cannot be more than 50 years and format 'YYYY-MM-DD': ")
    return birth_date


def set_type():
    animal_type = input("Enter the type of animal (dog, cat, hamster, horse, camel, donkey): ")
    while animal_type not in ("dog", "cat", "hamster", "horse", "camel", "donkey"):
        animal_type = input("Enter the type of animal (dog, cat, hamster, horse, camel, donkey): ")
    return animal_type
