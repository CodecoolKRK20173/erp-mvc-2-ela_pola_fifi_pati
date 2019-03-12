""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
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
    table.append(record)

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

    del table[int(id_)]

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

    remove(table, int(id_))
    table.insert(int(id_), record)

    return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    # your code

    
    counts_by_manufacturers = {}
    for game in table:
        manufacturer = game[2]

        if manufacturer in counts_by_manufacturers:
            counts_by_manufacturers[manufacturer] += 1

        else:
            counts_by_manufacturers[manufacturer] = 1

    return counts_by_manufacturers
  

        


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    # your code

    for game in table:
        games_in_stock = game[4]
        manufacturer_in_list = game[2]
        games_counter = 0
        sum_games_avb = 0
        if manufacturer_in_list == manufacturer:
            games_counter += 1
            sum_games_avb += int(games_in_stock)
    avg_games = sum_games_avb/games_counter
    return avg_games