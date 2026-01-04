# проверяем корректно ли работает метод def charge(self, user_id: str, amount_cents: int) -> str:
import pytest

from pricing.base_calculator import BaseCalculator
from providers.paypal_provider import PayPal
from providers.stripe_provider import Stripe
from services.payment_service import PaymentService

def test_charge_paypal(mocker):
    mock_provider = mocker.Mock(spec=PayPal)
    mock_provider.charge.return_value = 'ca444454-0a40-4cab-874e-692669bdfaf0'

    calculator = BaseCalculator()
    service = PaymentService(mock_provider, calculator)
    transaction_id = service.pay('12', 10.0)

    assert transaction_id == 'ca444454-0a40-4cab-874e-692669bdfaf0'
    mock_provider.charge.assert_called_once_with('12', 1000)


def test_charge_stripe(mocker):
    mock_provider = mocker.Mock(spec=Stripe)
    mock_provider.charge.return_value = '67e7cd6f-c6a2-44f7-b286-a51a0ef0824d'

    calculator = BaseCalculator()
    service = PaymentService(mock_provider, calculator)
    transaction_id = service.pay('111', 50.0)

    assert transaction_id == '67e7cd6f-c6a2-44f7-b286-a51a0ef0824d'
    mock_provider.charge.assert_called_once_with('111', 5000)