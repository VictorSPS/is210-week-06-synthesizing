#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""With lists and loop getting ready to send auto e-mails"""


def prepare_email(appointments):
    """Function takes one argument, uses a for loop and return the
        new list.
    Arg:
       appointments(mix): list of 2 tuples containing name and date.
    Return:
       returns a new list with the input names and dates.
    Example:
       >>> prepare_email([('Jack', 2015), ('Max', 'March 3')])
           ['Dear Jack,\nI look forward to meeting you on 2015. \nBest,\nMe',
           'Dear Max,\nI look forward to meeting you on March 3. \nBest,\nMe']
    """
    email = []
    list1 = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'
    for item in appointments:
        email.append(list1.format(item[0], item[1]))
    return email
