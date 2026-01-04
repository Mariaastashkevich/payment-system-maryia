from src.interfaces.price_calculator import PriceCalculator


class DiscountCalculator(PriceCalculator):
    def __init__(self, calculator: PriceCalculator, discount_rate: float):
        self.calculator = calculator
        self.discount_rate = discount_rate

    def calculate(self, price: float) -> float:
        base_price = self.calculator.calculate(price)
        return base_price * (1 - self.discount_rate * 0.01)
