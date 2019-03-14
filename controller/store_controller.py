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
            record = []
            index = 0
            inputs = terminal_view.get_inputs(title_list, title)
            for i in inputs:
                record.insert(index, i)
                index += 1
            store.add(table, record)
            data_manager.write_table_to_file(data_file, table)
            terminal_view.print_table(table, title_list)
            
        elif choice == "2":
            user_input = terminal_view.get_inputs(["Enter ID: "], "")
            store.remove(table, user_input[0])
            terminal_view.print_table(table, title_list)
        elif choice == "3":
            record = []
            index = 0
            user_input = terminal_view.get_inputs(["Enter ID: "], "")
            inputs = terminal_view.get_inputs(title_list, title)
            for i in inputs:
                record.insert(index, i)
                index += 1
            store.update(table, user_input[0], record)
            terminal_view.print_table(table, title_list)
        elif choice == "4":
            store.get_counts_by_manufacturers(table)
            terminal_view.print_result(store.get_counts_by_manufacturers(table), 'how many different kinds of game are available of each manufacturer: ')
        elif choice == "5":
            user_input = input('Enter manufacturer:')
            store.get_average_by_manufacturer(table, user_input)
            terminal_view.print_result(store.get_average_by_manufacturer(table, user_input), 'Average amount of games in stock. Manufacturer: ' + user_input)
        else:
            terminal_view.print_error_message("There is no such choice.")
