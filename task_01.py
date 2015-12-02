#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module uses arbitrary args."""


import pet


class Dog(pet.Pet):
    """Subclass from Pet class."""

    def __init__(self, has_shots=False, **kwargs):
        """A constructor.
        Args:
            has_shots(bool,optional): defaults to False
            kwargs: arbitrary arguments dicitonary

        Attributes:
            has_shots(bool): defaults to F.
        """
        self.has_shots = has_shots
        pet.Pet.__init__(self, **kwargs)
