import logging

from listeners.admin_alert_listener import AdminAlertListener
from listeners.log_listener import LogListener
from pricing.base_calculator import BaseCalculator
from pricing.discount_calculator import DiscountCalculator
from providers.stripe_provider import Stripe
from providers.paypal_provider import PayPal
from services.event_dispatcher import EventDispatcher
from services.payment_service import PaymentService
from pricing.tax_calculator import TaxCalculator
from logging_config import configure_logging
from src.events.event_type import EventType
from dotenv import load_dotenv
import os


def main():
    configure_logging(level=logging.INFO)
    load_dotenv()

    provider_name = os.getenv('PROVIDER', 'PayPal')
    tax_rate = float(os.getenv('TAX_RATE', 0))
    discount_rate = float(os.getenv('DISCOUNT_RATE', 0))

    provider = Stripe() if provider_name == 'Stripe' else PayPal()

    calculator = BaseCalculator()
    if tax_rate:
        calculator = TaxCalculator(
            calculator,
            tax_rate=tax_rate
        )
    if discount_rate:
        calculator = DiscountCalculator(
            calculator,
            discount_rate=discount_rate
        )

    dispatcher = EventDispatcher()
    dispatcher.attach(LogListener())
    dispatcher.attach(AdminAlertListener())

    service = PaymentService(provider, calculator, dispatcher)

    print(service.pay('12', 118))
    print(service.pay('111', 220))



if __name__ == "__main__":
    main()
