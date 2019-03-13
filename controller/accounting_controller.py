# everything you'll need is imported:
from view import terminal_view
from model.accounting import accounting
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
    title = "Accounting options"
    options = ["Add item",
               "Remove item",
               "Update item",
               "Which year has a maximum profit",
               "What is an avarange profit in a given year"]
    exit_message = "Back to main menu"

    title_list = [
        ['ID'],
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
            #rozpierdala tabelkę, zrobić backup pliku .csv
            record = terminal_view.get_inputs(["Month"] + ["Day"] + ["Year"] + ["Type"] + ["Amount"], "")
            accounting.add(table, record)
        elif choice == "2":
            accounting.remove()
        elif choice == "3":
            accounting.update()
        elif choice == "4":
            terminal_view.print_result(accounting.which_year_max(table), "Year with the highest income: ")
        elif choice == "5":
            year = terminal_view.get_inputs(['Year to get average: '], "")
            terminal_view.print_result(accounting.avg_amount(table, year[0]), "Average: ")
        else:
            terminal_view.print_error_message("There is no such choice.")

    # your code
