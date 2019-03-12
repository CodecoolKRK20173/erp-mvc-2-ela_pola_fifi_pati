""" Common functions for models
implement commonly used functions here
"""
import random


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = ''

    # your code

    
    special_characters = ['"', '!', '#', '$', '%', '&', '(', ')', '*', '+', '-','.', '/', ':', '<', '=', '>', '?', '@', '^', '~']
    numbers = []
    abc = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    abc_upper = []

    for i in range(0, 10):
        i = str(i)
        numbers.append(i)
    
    for i in abc:
        i = i.upper()
        abc_upper.append(i)


    generated = ''.join(
    random.choice(abc) + 
    random.choice(abc_upper)+ 
    random.choice(numbers) +
    random.choice(numbers) +
    random.choice(abc_upper) + 
    random.choice(abc) + 
    random.choice(special_characters) + 
    random.choice(special_characters) 
    )

    generated = table[0]

    return generated
