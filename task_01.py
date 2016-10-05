#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_01."""


def get_party_stats(families, table_size=6):
    """Function takes two parameters, uses the for loop
       and returns the results in a tuple
    Arg:
       families(str):a list of families which are, themselves, lists of
                      members.
       table_size(int): maximum number of seats at each table = 6.
    Return:
       returns the total number of guests and total tables needed.
    Examples:
       >>>get_party_stats([['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack',
           'Janis']])
       (6, 3)
       >>> get_party_stats([['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack',
           'Janis']], 2)
       (6, 4)
    """
    total_guests = 0
    total_tables = 0
    for people in families:
        family = len(people)
        total_guests += family
        total_tables += -(-family//table_size)

    return (total_guests, total_tables)
