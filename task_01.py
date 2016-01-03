#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Wk 14 warmup task 01."""

import pet


class Dog(pet.Pet):
    """A class that represents a dog."""

    def __init__(self, has_shots=False, **kwargs):
        """Constructor for the Dog class.
        Args:
            has_shots(boolean, optional): a boolean, defaults to False
            **kwargs: arbitrary arguments passed from parent pet.Pet class.
        """
        pet.Pet.__init__(self, **kwargs)
        self.has_shots = has_shots
