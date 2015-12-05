#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Using comprehension"""


from data import FRUIT


def get_cost_per_item(shoplist):
    """A function to get cost per item.

    Args:
        shoplist: A list of items.

    Returns:
        cost of each item.
    """
    return {key: FRUIT[key] * value for key, value in shoplist.iteritems()
            if key in FRUIT}


def get_total_cost(shoplist):
    """A function to calculate total cost.

    Args:
        shoplist: A list of items.

    Returns:
        total cost of items.
    """
    return sum(get_cost_per_item(shoplist).values())
