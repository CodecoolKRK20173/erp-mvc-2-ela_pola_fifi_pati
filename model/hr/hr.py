""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
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
    data_manager.write_table_to_file("model/hr/persons.csv", table)

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
    data_manager.write_table_to_file("model/hr/persons.csv", table)
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
    data_manager.write_table_to_file("model/hr/persons.csv", table)

    entry_index = 0
    for entry in table:
        entry_id_ = entry[0]
        if entry_id_ == id_:
            del table[entry_index]
        entry_index += 1

    return table

# special functions:
# ------------------


def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    list_of_oldest_people = []

    oldest_person_birthsday = int(table[0][2])

    for element in table:
        person_birthsday = int(element[2])
        if person_birthsday < oldest_person_birthsday:
            oldest_person_birthsday = person_birthsday

    for element in table:
        person_birthsday = int(element[2])
        if person_birthsday == oldest_person_birthsday:
            list_of_oldest_people.append(element[1])

    return list_of_oldest_people


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    years_summed = 0
    closest_to_average = []

    for element in table:
        years_summed = years_summed + int(element[2])

    years_average = years_summed / len(table)
    diff_from_average = abs(int(table[0][2]) - years_average)

    for element in table:
        if abs(int(element[2]) - years_average) < diff_from_average:
            diff_from_average = abs(int(element[2]) - years_average)

    for element in table:
        if abs(int(element[2]) - years_average) == diff_from_average:
            closest_to_average.append(element[1])

    return closest_to_average
