#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This uses comprehensions.."""


from data import FRUIT


def get_cost_per_item(shoplist):
    """Gives cost per item for dictionary keyed
    Args:
        Key of shoplist is item name (found in FRUIT)
        Value of shoplist is int (# of units to buy)
    Return:
        (dict): with name of fruit and total cost per item
    Example:
        >>> get_cost_per_item({'Lime': 12, 'Red Pear': 4, 'Peach': 24,
        'Beet': 1})
        {'Lime': 7.08, 'Peach': 95.76, 'Red Pear': 9.96}
    """
    return{item: FRUIT[item] * shoplist[item] for item in shoplist.iterkeys()
           if item in FRUIT}


def get_total_cost(shoplist):
    """Gives the total amount.
    Args:
        mylist(dict)
    Returns:
        total amount
    Examples:
        >>> get_total_cost({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
        112.80000000000001
    """
    return sum(listsum for listsum in get_cost_per_item(shoplist).itervalues())
