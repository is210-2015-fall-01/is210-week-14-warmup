#!user/bin/env python
# -*- coding: utf-8 -*-
"""Args"""

import pet

class Dog(pet.Pet):
    """Class docstring"""

    def __init__(self, has_shots=False, **kwargs):
        """Calls Pet class, multiple args.
        Args:
            has_shotts (bool)
            kwargs (multiple): may be multiple args from parent class
        Returns:
        Examples:
        """
        self.has_shots = has_shots
        pet.Pet.__init__(self, **kwargs)
