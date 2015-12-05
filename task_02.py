#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 14 warmup task_02."""

from data import FRUIT


def get_cost_per_item(shoplist):
    """This function return cost per item.

    Arguments:
        shoplist(dict): Dictionary items, fruits and prices.

    Return:
        Dictionary lists of fruits and it's values.

    Examples:
        >>> shoplist = {'Beet': 1, 'Apple': 2.08, 'Lime': 12, 'Peach': 24}
        >>> get_cost_per_item(shoplist)
        {'Peach': 95.76, 'Lime': 7.08}
    """
    return {key: shoplist[key] * FRUIT[key]
            for key in shoplist.iterkeys() if key in FRUIT}


def get_total_cost(shoplist):
    """This function returns total cost.

    Args:
        shoplist(dict): dictionary item.

    Return:
        returns total cost for dictionary item.

    Examples:
        >>> shoplist = {'Beet': 1, 'Apple': 2.08, 'Lime': 12, 'Peach': 24}
        >>> get_total_cost(shoplist)
        102.84
    """
    return sum(val for val in get_cost_per_item(shoplist).itervalues())
