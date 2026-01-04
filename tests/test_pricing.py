import pytest

from pricing.base_calculator import BaseCalculator
from pricing.discount_calculator import DiscountCalculator
from pricing.tax_calculator import TaxCalculator


@pytest.fixture
def base_calculator():
    return BaseCalculator()

def test_base_calculator(base_calculator):
    assert base_calculator.calculate(100) == 100
    assert base_calculator.calculate(2000) == 2000
    assert base_calculator.calculate(456771) == 456771


def test_discount_calculator(base_calculator):
    assert DiscountCalculator(base_calculator, discount_rate=20).calculate(100) == 80
    assert DiscountCalculator(base_calculator, discount_rate=10).calculate(1000) == 900
    assert DiscountCalculator(base_calculator, discount_rate=50).calculate(100) == 50


def test_tax_calculator(base_calculator):
    assert TaxCalculator(base_calculator, tax_rate=10).calculate(100) == pytest.approx(110)
    assert TaxCalculator(base_calculator, tax_rate=13).calculate(100) == pytest.approx(113)
    assert TaxCalculator(base_calculator, tax_rate=20).calculate(1000) == pytest.approx(1200)


def test_tax_calculator_with_discount(base_calculator):
    assert TaxCalculator(
        DiscountCalculator(
            base_calculator,
            discount_rate=20),
        tax_rate=10).calculate(100) == pytest.approx(88)
    assert TaxCalculator(
        DiscountCalculator(
            base_calculator,
            discount_rate=50),
        tax_rate=13).calculate(1000) == pytest.approx(565)

