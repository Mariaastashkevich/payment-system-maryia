from listeners.admin_alert_listener import AdminAlertListener
from listeners.log_listener import LogListener
from pricing.tax_calculator import TaxCalculator
from services.event_dispatcher import EventDispatcher
from src.events.event_type import EventType
from src.interfaces.payment_provider import PaymentProvider
from src.interfaces.price_calculator import PriceCalculator


class PaymentService:
    def __init__(self, payment_provider: PaymentProvider, calculator: PriceCalculator, dispatcher: EventDispatcher):
        self.payment_provider = payment_provider
        self.calculator = calculator
        self.dispatcher = dispatcher

    def pay(self, user_id: str, base_price: float) -> str | None:
        price = self.calculator.calculate(base_price)
        try:
            transaction_id =  self.payment_provider.charge(user_id, int(price * 100))
            self.dispatcher.notify(
                {
                    'type': EventType.PAYMENT_SUCCESS.value,
                    'user_id': user_id,
                    'amount': price
                }
            )
            return transaction_id
        except Exception as e:
            self.dispatcher.notify(
                {
                    'type': EventType.PAYMENT_FAILURE.value,
                    'user_id': user_id,
                    'amount': price
                }
            )
        return None

