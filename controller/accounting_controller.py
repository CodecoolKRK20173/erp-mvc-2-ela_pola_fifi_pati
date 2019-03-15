# everything you'll need is imported:
from view import terminal_view
from model.accounting import accounting
from model import data_manager


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    title = "Accounting options"
    options = ["Add item",
               "Remove item",
               "Update item",
               "Which year has a maximum profit",
               "What is an avarange profit in a given year"]
    exit_message = "Back to main menu"

    title_list = [
        ['Month'],
        ['Day'],
        ['Year'],
        ['Type'],
        ['Amount']]

    data_file = "model/accounting/items.csv"
    table = data_manager.get_table_from_file(data_file)
    terminal_view.print_table(table, title_list)
    #
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
            accounting.add(table, record)
            data_manager.write_table_to_file(data_file, table)
            terminal_view.print_table(table, title_list)

        elif choice == "2":
            user_input = terminal_view.get_inputs(["Enter ID: "], "")
            accounting.remove(table, user_input[0])
            terminal_view.print_table(table, title_list)

        elif choice == "3":
            record = []
            index = 0
            user_input = terminal_view.get_inputs(["Enter ID: "], "")
            inputs = terminal_view.get_inputs(title_list, title)
            for i in inputs:
                record.insert(index, i)
                index += 1
            accounting.update(table, user_input[0], record)
            terminal_view.print_table(table, title_list)
        elif choice == "4":
            terminal_view.print_result(accounting.which_year_max(
                table), "Year with the highest income: ")
        elif choice == "5":
            year = terminal_view.get_inputs(['Year to get average: '], "")
            terminal_view.print_result(
                accounting.avg_amount(table, year[0]), "Average: ")
        else:
            terminal_view.print_error_message("You have chosen back to menu.")

    # exchanged "There is no such choice." into
