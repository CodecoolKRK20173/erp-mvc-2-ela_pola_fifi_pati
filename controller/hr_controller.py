# everything you'll need is imported:
from view import terminal_view
from model.hr import hr
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

    title = "Human resources manager"
    options = ["Add item",
                "Remove item",
                "Update item",
                "Show the oldest person",
                "Show person closest to average age"]
    exit_message = "Back to main menu"

    title_list = [
        ['ID'],
        ['Name'],
        ['Date of birth']]

    
    data_file = "model/hr/persons.csv"
    table = data_manager.get_table_from_file(data_file)
    terminal_view.print_table(table, title_list)
    
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(title, options, exit_message)
        if choice == "1":
            hr.add()
        elif choice == "2":
            hr.remove()
        elif choice == "3":
            hr.update()
        elif choice == "4":
            hr.get_oldest_person()
        elif choice == "5":
            hr.get_persons_closest_to_average()
        else:
            terminal_view.print_error_message("There is no such choice.")
