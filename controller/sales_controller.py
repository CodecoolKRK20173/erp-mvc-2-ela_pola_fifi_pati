# everything you'll need is imported:
from view import terminal_view
from model.sales import sales
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
            record = []
            index = 0
            inputs = terminal_view.get_inputs(title_list, title)
            for i in inputs:
                record.insert(index, i)
                index += 1
            sales.add(table, record)
            data_manager.write_table_to_file(data_file, table)
            terminal_view.print_table(table, title_list)

        elif choice == "2":
            user_input = terminal_view.get_inputs(["Enter ID: "], "")
            sales.remove(table, user_input[0])
            terminal_view.print_table(table, title_list)
        elif choice == "3":
            record = []
            index = 0
            user_input = terminal_view.get_inputs(["Enter ID: "], "")
            inputs = terminal_view.get_inputs(title_list, title)
            for i in inputs:
                record.insert(index, i)
                index += 1
            sales.update(table, user_input[0], record)
            terminal_view.print_table(table, title_list)
        elif choice == "4":
            terminal_view.print_result(sales.get_lowest_price_item_id(
                table), "ID of item with lowest price")
        elif choice == "5":
            month_from = terminal_view.get_inputs(["Month from:"], "")
            day_from = terminal_view.get_inputs(["Day from:"], "")
            year_from = terminal_view.get_inputs(["Year from:"], "")
            month_to = terminal_view.get_inputs(["Month to:"], "")
            day_to = terminal_view.get_inputs(["Day to:"], "")
            year_to = terminal_view.get_inputs(["Year to:"], "")

            terminal_view.print_result(sales.get_items_sold_between(
                table, month_from[0], day_from[0], year_from[0], month_to[0], day_to[0], year_to[0]), "Items sold in cetrain time")
        else:
            terminal_view.print_error_message("You have chosen back to menu.")
