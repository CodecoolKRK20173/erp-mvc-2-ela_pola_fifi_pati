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
            record = []
            index = 0
            inputs = terminal_view.get_inputs(title_list, title)
            for i in inputs:
                record.insert(index, i)
                index += 1
            crm.add(table, record)
            data_manager.write_table_to_file(data_file, table)
            terminal_view.print_table(table, title_list)
            
        elif choice == "2":
            user_input = terminal_view.get_inputs(["Enter ID: "], "")
            crm.remove(table, user_input[0])
            terminal_view.print_table(table, title_list)
        elif choice == "3":
            record = []
            index = 0
            user_input = terminal_view.get_inputs(["Enter ID: "], "")
            inputs = terminal_view.get_inputs(title_list, title)
            for i in inputs:
                record.insert(index, i)
                index += 1
            crm.update(table, user_input[0], record)
            terminal_view.print_table(table, title_list)
        elif choice == "4":
            terminal_view.print_result(crm.get_longest_name_id(table), "This is the longest ID")
        elif choice == "5":
            terminal_view.print_result(crm.get_subscribed_emails(table), "Subscribed e-mails")
        else:
            terminal_view.print_error_message("You have chosen back to menu.")
