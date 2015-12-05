#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is task_02 docstring."""


from data import FRUIT


def get_cost_per_item(shoplist):
    """Get shopping list.

    Args:
        shoplist (dictionary): A dictionary with items from data module

    Returns:
        A dictionary of shoplist.

    Example:
        >>> get_cost_per_item({'Lime': 12, 'Red Pear': 4,
                               'Peach': 24,'Beet': 1})
        {'Lime': 7.08, 'Peach': 95.76, 'Red Pear': 9.96}
    """
    return {item: FRUIT[item] * shoplist[item] for item in shoplist.iterkeys()
            if item in FRUIT}


def get_total_cost(shoplist):
    """Get total cost of shopping list.

    Args:
        shoplist (dictionary): A dictionary with items from data module.
        mylist (dictionary): The shopping list.

    Return:
        Grant total of shopping list.

    Example:
        >>> get_total_cost({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
        112.80000000000001
    """
    mylist = get_cost_per_item(shoplist)
    return sum([value for value in mylist.values()])
