from __future__ import annotations
from abc import ABC, abstractmethod


class Menu(ABC):

    @abstractmethod
    def run(self, registry) -> Menu:
        pass
