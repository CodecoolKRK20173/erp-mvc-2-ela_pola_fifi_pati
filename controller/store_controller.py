# everything you'll need is imported:
from model.store import store
from view import terminal_view
from controller import common
from model import data_manager


def run():

    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
        """

    title = "Store manager"
    options = ["Add item",
                "Remove item",
                "Update item",
                "Show how many different kinds of game are available of each manufacturer",
                "Show average amount of games in stock of a given manufacturer"]
    exit_message = "Back to main menu"
    
    title_list = [
        ['ID'],
        ['Name'],
        ['Manufacturer'],
        ['Price'],
        ['Number in stock']]

    
    data_file = "model/store/games.csv"
    table = data_manager.get_table_from_file(data_file)
    terminal_view.print_table(table, title_list)

    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(title, options, exit_message)
        if choice == "1":
            store.add()
        elif choice == "2":
            store.remove()
        elif choice == "3":
            store.update()
        elif choice == "4":
            store.get_counts_by_manufacturers()
        elif choice == "5":
            store.get_average_by_manufacturer()
        else:
            terminal_view.print_error_message("There is no such choice.")
