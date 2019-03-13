# everything you'll need is imported:
from view import terminal_view
from model.inventory import inventory
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

    title = "Inventory manager"
    options = ["Add item",
                "Remove item",
                "Update item",
                "Show items that have not exceeded their durability",
                "Show average durability times for each manufacturer"]
    exit_message = "Back to main menu"

    title_list = [
        ['Product'],
        ['Manufacturer'],
        ['Purchase year'],
        ['Durability']]

    
    data_file = "model/inventory/inventory.csv"
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
            inventory.add(table, record)
            data_manager.write_table_to_file(data_file, table)
            terminal_view.print_table(table, title_list)
            
        elif choice == "2":
            user_input = input('Enter ID:')
            inventory.remove(table, user_input)
            terminal_view.print_table(table, title_list)
        elif choice == "3":
            inventory.update()
        elif choice == "4":
            terminal_view.print_result(inventory.get_available_items(table), "Available items")
        elif choice == "5":
            terminal_view.print_result(inventory.get_average_durability_by_manufacturers(table), "Average durability by manufacturers")
        else:
            terminal_view.print_error_message("There is no such choice.")
