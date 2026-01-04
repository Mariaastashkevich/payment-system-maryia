from pricing.base_calculator import BaseCalculator
from providers.paypal_provider import PayPal
from services.payment_service import PaymentService


def test_payment_service(mocker):
    mock_provider = mocker.Mock(spec=PayPal)
    mock_calculator = mocker.Mock(spec=BaseCalculator)

    mock_calculator.calculate.return_value = 100
    mock_provider.charge.return_value = 10000

    service = PaymentService(mock_provider, mock_calculator)
    result = service.pay('1', 100)

    assert result == 10000
    mock_calculator.calculate.assert_called_once_with(100)
    mock_provider.charge.assert_called_once_with('1', 10000)