from animal_registry.presenters.methods import Methods


class MenuPresenter(Methods):
    def __init__(self, view):
        super().__init__(view)
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
