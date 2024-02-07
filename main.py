from animal_registry.views.menu_view import MenuView
from animal_registry.presenters.menu_presenter import MenuPresenter


def main():
    view = MenuView()
    presenter = MenuPresenter(view)

    while True:
        view.show_menu()
        choice = view.get_choice()
        presenter.handle_choice(choice)

        if choice == "6":
            break


if __name__ == "__main__":
    main()
