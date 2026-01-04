from abc import ABC, abstractmethod


class PriceCalculator(ABC):
    @abstractmethod
    def calculate(self, price: float) -> float:
        pass