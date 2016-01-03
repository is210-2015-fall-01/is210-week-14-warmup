#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is task_01 docstring."""

import pet


class Dog(pet.Pet):
    """A Dog class that inherits from the Pet class."""

    def __init__(self, has_shots=False, **kwargs):
        """Constructor function.

        Args:
            has_shots (boolean): Optional (Default: False)
            **kwargs: Arbitrary argument dictionary

        Attributes:
            has_shots (boolean): Optional (Default: False)
"""
        self.has_shots = has_shots
        pet.Pet.__init__(self, **kwargs)
