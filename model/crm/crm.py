""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
"""

# everything you'll need is imported:
from model import data_manager
from model import common
import os


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
    data_manager.write_table_to_file("model/crm/customers.csv", table)

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

    for entry in table:
        entry_id_ = entry[0]
        if entry_id_ == id_:
            entry = record

    return table


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """

    longest_name = table[0][1]  # takes the ID and name of first customer
    for element in table:
        element_name = element[1]
        if len(element_name) > len(longest_name):
            longest_name = element_name
            id_ = element[0]
        elif len(element_name) == len(longest_name) and element_name > longest_name:
            longest_name = element_name
            id_ = element[0]
            os.system("clear")
    return id_


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """

    subscriptions_list = []   
    for element in table:
        subscription = int(element[3])
        if subscription == 1:
            subscriptions_list.append(element[2] + ";" + element[1])
           
    return subscriptions_list

# for testing: 
# pri..(get_subscribed_emails(data_manager.get_table_from_file("model/crm/customers.csv")))