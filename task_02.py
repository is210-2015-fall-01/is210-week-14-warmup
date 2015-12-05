#!user/bin/env python
# -*- coding: utf-8 -*-
"""Args"""

from data import FRUIT


def get_cost_per_item(shoplist):
    """Creates new dict based on items in FRUIT dict and input amount.
    Args:
        shoplist (dict): Item in FRUIT (key) and amount as an int (value)
    Returns:
        New dict showing total price for each item
    Examples:
    >>>get_cost_per_item({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
    {'Lime': 7.08, 'Peach': 95.76, 'Red Pear': 9.96}
    """

    price_dict = {item: FRUIT[item] * shoplist[item]

                  for item in shoplist.iterkeys() if item in FRUIT}
    return price_dict


def get_total_cost(shoplist):
    """Sums total prices of each item based on output of get_cost_per_item
    Args:
        shoptlist (dict): item in FRUIT (key) and amount as an int (value)
    Returns:
        Total price of items summed together
    Examples:
        >>>get_total_cost({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
        112.80000000000001
    """
    price_dict = get_cost_per_item(shoplist)
    total_dict = sum([item for item in price_dict.itervalues()])
    return total_dict
