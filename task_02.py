#! usr/bin/env python
# -*- coding: utf-8 -*-
"""A module for shopping."""

from data import FRUIT


def get_cost_per_item(shoplist):
    """A shopping list.

    Args:
       The key of shoplist should be the item name as found in FRUIT.
       The value of shoplist should be an integer indicating the number
       of units to purchase.

    Return:
        A new dict keyed by the name of fruit showing total cost per item.

    Example:
        >>> get_cost_per_item({'Lime': 12, 'Red Pear': 4, 'Peach': 24,
                               'Beet': 1})
        {'Lime': 7.08, 'Peach': 95.76, 'Red Pear': 9.96}
    """
    return {item: FRUIT[item] * shoplist[item] for item in shoplist.iterkeys()
            if item in FRUIT}


def get_total_cost(shoplist):
    """Total cost for shoplist.
    Args:
        mylist(dict): a shopping list.
    Return:
        The total cost of my shopping list.
    Example:
        >>> get_total_cost({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
        112.80000000000001
    """
    mylist = get_cost_per_item(shoplist)
    return sum([value for value in mylist.values()])
