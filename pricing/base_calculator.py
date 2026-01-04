from src.interfaces.price_calculator import PriceCalculator


class BaseCalculator(PriceCalculator):
    def calculate(self, price: float) -> float:
        return price
