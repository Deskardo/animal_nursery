class Animal:
    count = 0

    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
        Animal.count += 1

    def sound(self):
        pass

    def commands(self):
        pass