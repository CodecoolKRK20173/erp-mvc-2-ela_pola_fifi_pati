# everything you'll need is imported:
from view import terminal_view
from model.crm import crm
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

    title = "Customer Relationship Management (CRM)"
    options = ["Add item",
                "Remove item",
                "Update item",
                "Longest ID of customer",
                "Show subscibers"]
    exit_message = "Back to main menu"

    title_list = [
        ['ID'],
        ['Name'],
        ['E-mail address'],
        ['Subscription']]

    
    data_file = "model/crm/customers.csv"
    table = data_manager.get_table_from_file(data_file)
    terminal_view.print_table(table, title_list)

    
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(title, options, exit_message)
        if choice == "1":
            crm.add()
        elif choice == "2":
            crm.remove()
        elif choice == "3":
            crm.update()
        elif choice == "4":
            crm.get_longest_name_id()
        elif choice == "5":
            crm.get_subscribed_emails()
        else:
            terminal_view.print_error_message("There is no such choice.")
