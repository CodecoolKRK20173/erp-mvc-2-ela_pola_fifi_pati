""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
"""

# everything you'll need is imported:
from model import data_manager
from model import common


def add(table, record):
    """
    Add new record to table

    Args:
        table (list): table to add new record to
        record (list): new record

    Returns:
        list: Table with a new record
    """
    index_id = 0
    record.insert(index_id, common.generate_random(table))
    table.append(record)
    data_manager.write_table_to_file("model/sales/sales.csv", table)

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    entry_index = 0
    for entry in table:
        entry_id_ = entry[0]
        if entry_id_ == id_:
            del table[entry_index]
        entry_index += 1
    data_manager.write_table_to_file("model/sales/sales.csv", table)
    return table


def update(table, id_, record):
    """
    Updates specified record in the table.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update
        record (list): updated record

    Returns:
        list: table with updated record
    """

    index_id = 0
    record.insert(index_id, common.generate_random(table))
    table.append(record)
    data_manager.write_table_to_file("model/sales/sales.csv", table)

    entry_index = 0
    for entry in table:
        entry_id_ = entry[0]
        if entry_id_ == id_:
            del table[entry_index]
        entry_index += 1

    return table

# special functions:
# ------------------


def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    index_index = 0
    index_title = 1
    index_price = 2
    index_first_game = 0
    min_price = int(table[index_first_game][index_price])
    lowest_price_games = []
    for game in table:
        if int(game[index_price]) < min_price:
            min_price = int(game[index_price])
    for game in table:
        if int(game[index_price]) == min_price:
            lowest_price_games.append(game)
    if len(lowest_price_games) > 1:
        list_titles = sort_my([game[index_title] for game in lowest_price_games])
        for game in lowest_price_games:
            if game[index_title] == list_titles[-1]:
                return game[index_index]
    return lowest_price_games[index_index][index_index]


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """
    filtered_table = []
    month_from = str(month_from)
    month_to = str(month_to)
    day_from = str(day_from)
    day_to = str(day_to)
    year_from = str(year_from)
    year_to = str(year_to)
    if len(month_to) == 1:
        month_to = "0" + month_to
    if len(month_from) == 1:
        month_from = "0" + month_from
    if len(day_to) == 1:
        day_to = "0" + day_to
    if len(day_from) == 1:
        day_from = "0" + day_from
    from_number = int(year_from + month_from + day_from)
    to_number = int(year_to + month_to + day_to)

    for element in table[:]:
        if len(element[3]) == 1:
            element[3] = "0" + element[3]
        if len(element[4]) == 1:
            element[4] = "0" + element[4]
        item_number = int(element[5] + element[3] + element[4])
        if item_number > from_number and item_number < to_number:
            filtered_table.append(element)

    for i in range(len(filtered_table)):
        filtered_table[i][2] = int(filtered_table[i][2])
        filtered_table[i][3] = int(filtered_table[i][3])
        filtered_table[i][4] = int(filtered_table[i][4])
        filtered_table[i][5] = int(filtered_table[i][5])
    return filtered_table
