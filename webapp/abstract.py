"""
An abstract class cannot be initialised. It is only used to serve as a class for the
automation path in the main.py, when used the if statements as filters
"""

from abc import ABC, abstractmethod


class AbstractPage(ABC):

    @abstractmethod
    def serve(self):
        pass