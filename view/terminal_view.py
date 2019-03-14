""" Terminal view module """


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    item_index = 0
    title_index = 0
    titles = []
    for title in title_list:
        titles.append(title[title_index])
    titles.insert(0, "ID")

    col_width = []
    for title in titles:
        col_width.append(len(title))
    for items in table:
        for i, item in enumerate(items):
            if col_width[i] < len(str(item)):
                col_width[i] = len(str(item))
    table_width = 0

    for width in col_width:
        table_width += width + 3
    print("-" * table_width)


    for items in table:
        print("|", end="")
        for i, item in enumerate(items):
            print(' {:^{width}} |'.format(item, width=col_width[i]), end="")
        print()
        print("-" * table_width)


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print("\n" + label)
    if type(result) == list:
        print("")
        for element in result:
            print(element)
        print("")
    elif type(result) == dict:
        for key, value in result.items():
            print(key, value)
        print("")
    else:
        print(result)
    print("")


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print(title + ':')
    i = 1
    for element in list_options:
        print('\t' + str([i]) + ' ' + element)
        i += 1
    print('\t[0] ' + exit_message)


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []
    index = 0

    for element in list_labels:
        x = input(element)
        inputs.insert(index, x)
        index += 1

    return inputs


def get_choice(title, options, exit_message):
    print_menu(title, options, exit_message)
    inputs = get_inputs(["Please enter a number: "], "")
    return inputs[0]


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print("\n" + str(message))
