#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 14 Warmup Task 1."""

import pet


class Dog(pet.Pet):
    """A classy dog."""

    def __init__(self, has_shots=False, **kwargs):
        """Constructor for the classy dog.
        Args:
            has_shots(bool): boolean, defaults to False
            **kwargs: arbitrary arguments passed from parent pet.Pet class.
        """
        pet.Pet.__init__(self, **kwargs)
        self.has_shots = has_shots
