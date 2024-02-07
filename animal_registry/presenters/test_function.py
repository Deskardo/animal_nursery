import string
from datetime import datetime, timedelta
from animal_registry.models.animals import Animal


def is_correct_name(name: str) -> bool:
    if not name:
        return False
    return all([name.isalpha(), len(name) > 2, all([c in string.ascii_letters for c in name])])


def is_correct_date(date: str) -> bool:
    pattern = '%Y-%m-%d'
    if not date:
        return False
    try:
        date = datetime.strptime(date, pattern)
    except ValueError:
        return False
    return date + timedelta(days=18250) >= datetime.today()


def is_pets(animal_type: str) -> bool:
    return animal_type in ['dog', 'cat', 'hamster']


def is_name_in_registry(animal_type, name: str, registry: list) -> bool:
    name_type_filter = lambda x: x.type_of_pet == animal_type and x.name == name
    if not registry:
        return False
    elif len(list(filter(name_type_filter, registry))):
        return True
    return False
