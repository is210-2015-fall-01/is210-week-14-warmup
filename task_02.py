#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Wk14 warmup task 02."""

from data import FRUIT


def get_cost_per_item(shoplist):
    """A function that calculates the cost per item on a shopping list.
    Args:
        shoplist(dict):the key is item name from FRUIT and its value is an
            integer which indicates no. of units to be purchased
    Return:
        returns a dictionary keyed by name of fruit with total cost per item
            reflected.
    Examples:
        >>> shoplist = {'Beet': 1, 'Apple': 2.08, 'Lime': 12, 'Peach': 24}
        >>> get_cost_per_item(shoplist)
    {'Peach': 95.76, 'Lime': 7.08}
    """
    return {key: shoplist[key] * FRUIT[key]
            for key in shoplist.iterkeys() if key in FRUIT}


def get_total_cost(shoplist):
    """A function that gets the total cost.
    Args:
        shoplist(dict): key of shoplist is item found in FRUIT and value
            is an integer indicating no. of units to be purchased
    Return:
        returns the total cost by adding up values of resultant dictionary
    Examples:
        >>> shoplist = {'Beet': 1, 'Apple': 2.08, 'Lime': 12, 'Peach': 24}
        >>> get_total_cost(shoplist)
    102.84
    """
    return sum(someval for someval in get_cost_per_item(shoplist).itervalues())
