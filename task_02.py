#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 14 Warmup Task02."""

from data import FRUIT


def get_cost_per_item(shoplist):
    """Dictionary of fruits and price.
    Args:
        shoplist(dict): The key of shoplist should be the item name as
        found in FRUIT. The value of shoplist should be an integer
        indicating the number of units to purchase.

    Returns: a list of fruits with prices.
    Example: >>> get_cost_per_item({'Lime': 12, 'Red Pear': 4,
                                    'Peach': 24, 'Beet': 1})
                 {'Lime': 7.08, 'Peach': 95.76, 'Red Pear': 9.96}
    """
    return {key: FRUIT[key] * shoplist[key] for key in shoplist.iterkeys()
            if key in FRUIT}


def get_total_cost(shoplist):
    """Provides total cost.
    Args:
        shoplist(dict): The key of shoplist should be the item name as
        found in FRUIT. The value of shoplist should be an integer
        indicating the number of units to purchase.

    Returns: Total cost.
    Example: >>> get_total_cost({'Lime': 12, 'Red Pear': 4,
                                'Peach': 24, 'Beet': 1})
                 112.80000000000001
    """

    return sum(listval for listval in get_cost_per_item(shoplist).itervalues())
