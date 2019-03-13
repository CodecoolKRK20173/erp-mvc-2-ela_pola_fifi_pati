# everything you'll need is imported:
from view import terminal_view
from model.sales import sales
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

    title = "Sales manager"
    options = ["Add item",
                "Remove item",
                "Update item",
                "Show ID of item sold for lowest price",
                "Show item sold between certain dates"]
    exit_message = "Back to main menu"

    title_list = [
        ['ID'],
        ['Title'],
        ['Price'],
        ['Month'],
        ['Day'],
        ['Year']]

    
    data_file = "model/sales/sales.csv"
    table = data_manager.get_table_from_file(data_file)
    terminal_view.print_table(table, title_list)

    
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(title, options, exit_message)
        if choice == "1":
            sales.add()
        elif choice == "2":
            sales.remove()
        elif choice == "3":
            sales.update()
        elif choice == "4":
            sales.get_lowest_price_item_id()
        elif choice == "5":
            sales.get_items_sold_between()
        else:
            terminal_view.print_error_message("There is no such choice.")
