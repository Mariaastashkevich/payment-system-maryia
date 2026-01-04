from src.interfaces.price_calculator import PriceCalculator


class TaxCalculator(PriceCalculator):
    def __init__(self, calculator: PriceCalculator, tax_rate: float):
        self.calculator = calculator
        self.tax_rate = tax_rate

    def calculate(self, price: float) -> float:
        base_price = self.calculator.calculate(price)
        return base_price * (1 + (self.tax_rate * 0.01))
