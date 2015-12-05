#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Using arbitrary arguments"""


import pet


class Dog(pet.Pet):
    """A class that stores Dog data, and imports from pet module."""

    def __init__(self, has_shots=False, **kwargs):
        """Constructor for the Dog class.

        Args:
            has_shots (bool): Defaults to False.
            **kwargs : Arbitrary keyword arguments.

        Attributes:
            has_shots (bool): Defaults to False.
        """

        self.has_shots = has_shots
        pet.Pet.__init__(self, **kwargs)
