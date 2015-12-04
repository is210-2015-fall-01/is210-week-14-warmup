#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task 01"""

import pet


class Dog(pet.Pet):
    """Subclass from Pet Class."""

    def __init__(self, has_shots=False, **kwargs):
        """Constructor.

        Args:
            has_shots (bool): Default set to False.
            kwargs: Arbitary arg.

        Attributes:
            has_shots(bool): Default set to False.
        """
        self.has_shots = has_shots
        pet.Pet.__init__(self, **kwargs)
