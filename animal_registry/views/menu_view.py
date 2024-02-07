class MenuView:
    def show_menu(self):
        print("\n--- Animal Registry Menu ---")
        print("1. Add new animal")
        print("2. List commands for an animal")
        print("3. Train new commands for an animal")
        print("4. List animals by birth date")
        print("5. Show count of animals")
        print("6. Exit")

    def get_choice(self):
        return input("Enter your choice (1-6): ")