#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 14 warmup task_01."""

import pet


class Dog(pet.Pet):
    """Dog class from pet module.

    Attribute:
        None
    """
    def __init__(self, has_shots=False, **kwargs):
        """Constructor for the Dog class.

        Args:
            has_shots(bool): defaults to False.
            **kwargs(mix): an arbitrary arguments.

        Return:
            None.
        """
        pet.Pet.__init__(self, **kwargs)
        self.has_shots = has_shots
