# everything you'll need is imported:
from view import terminal_view
from model.accounting import accounting
from controller import common

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
    
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(title, options, exit_message)
        if choice == "1":
            accounting.add()
        elif choice == "2":
            accounting.remove()
        elif choice == "3":
            accounting.update()
        elif choice == "4":
            accounting.which_year_max()
        elif choice == "5":
            accounting.avg_amount()
        else:
            terminal_view.print_error_message("There is no such choice.")
                
   
    # your code
