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
        ['Name'],
        ['Date of birth']]

    
    data_file = "model/hr/persons.csv"
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
            hr.add(table, record)
            data_manager.write_table_to_file(data_file, table)
            terminal_view.print_table(table, title_list)
            
        elif choice == "2":
            user_input = terminal_view.get_inputs(["Enter ID: "], "")
            hr.remove(table, user_input[0])
            terminal_view.print_table(table, title_list)
        elif choice == "3":
            record = []
            index = 0
            user_input = terminal_view.get_inputs(["Enter ID: "], "")
            inputs = terminal_view.get_inputs(title_list, title)
            for i in inputs:
                record.insert(index, i)
                index += 1
            hr.update(table, user_input[0], record)
            terminal_view.print_table(table, title_list)
        elif choice == "4":
            terminal_view.print_result(hr.get_oldest_person(table), "Oldest person")
        elif choice == "5":
            terminal_view.print_result(hr.get_persons_closest_to_average(table), "Person closest to average")
        else:
            terminal_view.print_error_message("There is no such choice.")
