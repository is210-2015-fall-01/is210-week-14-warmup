#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task 02"""

from data import FRUIT


def get_cost_per_item(shoplist):
    """Shopping list.

    Args:
        shoplist (dict): items in shopping list.

    Return:
        a new dict with fruit and cost per item.

    Example:
    
    """
    return {item: FRUIT[item] * shoplist[item] for item in shoplist.iterkeys()
            if item in FRUIT}

def get_total_cost(shoplist):
    """Total cost for items in dict.

    Args:
        mylist (dict): a list.

    Return:
        The total cost of items in shopping list.

    Example:
        >>> print shoplist
        {'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1}
        >>> get_cost_per_item({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
        {'Lime': 7.08, 'Peach': 95.76, 'Red Pear': 9.96}
        >>> get_total_cost({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
        112.80000000000001
    
    """
    mylist = get_cost_per_item(shoplist)
    return sum([value for value in mylist.values()])
