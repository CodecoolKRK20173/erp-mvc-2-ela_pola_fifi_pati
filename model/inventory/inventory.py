""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
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

def get_available_items(table):
    """
    Question: Which items have not exceeded their durability yet?

    Args:
        table (list): data table to work on

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    # your code
    index_year = 3
    index_dur = 4
    available_items = []

    for item in table:
        item[index_year] = int(item[index_year])
        year = int(item[index_year])
        item[index_dur] = int(item[index_dur])
        dur = int(item[index_dur])

        if year + dur >= 2017:  
            available_items.append(item)
            
    return available_items



def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    # your code
    index_man = 2
    index_dur = -1
    list_of_manufacturer = set([item[index_man] for item in table])
    average_dur_dict = {item: 0 for item in list_of_manufacturer}
    for item in table:
        average_dur_dict[item[index_man]] += int(item[index_dur])

    for item in average_dur_dict.keys():
        counter_occurs = 0

        for item2 in table:

            if item2[index_man] == item:
                counter_occurs += 1

        average_dur_dict[item] /= counter_occurs

    return average_dur_dict

