# Payment System

A modular, extensible payment processing system built with Python that supports multiple payment providers and flexible price calculation strategies.

## Features

- **Multi-Provider Support**: Unified interface for payment providers (Stripe, PayPal) with easy extensibility
- **Modular Price Calculation**: Composable pricing logic with support for taxes, discounts, and custom calculations
- **Event-Driven Architecture**: Observer pattern implementation for payment events (success, failure, alerts)
- **Dependency Injection**: Loose coupling between components, making the system highly testable and maintainable
- **Logging & Monitoring**: Built-in logging and admin alert listeners for payment events

## Architecture

The system follows clean architecture principles with clear separation of concerns:

- **Interfaces**: Abstract base classes define contracts for payment providers and price calculators
- **Providers**: Concrete implementations of payment providers (Stripe, PayPal)
- **Pricing**: Composable price calculators using the Decorator pattern
- **Services**: Core payment service that orchestrates providers and calculators
- **Events**: Event-driven notifications for payment lifecycle events
- **Listeners**: Observers that react to payment events (logging, admin alerts)

## Project Structure

```
payment-system-maryia/
├── src/
│   ├── interfaces/          # Abstract base classes
│   │   ├── payment_provider.py
│   │   ├── price_calculator.py
│   │   └── event_listener.py
│   └── events/
│       └── event_type.py    # Event type definitions
├── providers/               # Payment provider implementations
│   ├── stripe_provider.py
│   └── paypal_provider.py
├── pricing/                 # Price calculation modules
│   ├── base_calculator.py
│   ├── tax_calculator.py
│   └── discount_calculator.py
├── services/                # Core business logic
│   ├── payment_service.py
│   └── event_dispatcher.py
├── listeners/               # Event listeners
│   ├── log_listener.py
│   └── admin_alert_listener.py
├── tests/                   # Test suite
├── main.py                  # Application entry point
└── logging_config.py        # Logging configuration
```

## Installation

1. **Prerequisites**: Python 3.10 or higher

2. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd payment-system-maryia
   ```

3. **Install dependencies**:
   ```bash
   # Using uv (recommended)
   uv sync
   
   # Or using pip
   pip install -r requirements.txt
   ```

## Configuration

Create a `.env` file in the project root to configure the system:

```env
# Payment provider: 'Stripe' or 'PayPal'
PROVIDER=PayPal

# Tax rate (0.0 to 1.0, e.g., 0.1 for 10%)
TAX_RATE=0.0

# Discount rate (0.0 to 1.0, e.g., 0.15 for 15%)
DISCOUNT_RATE=0.0
```

## Usage

### Basic Example

```python
from services.payment_service import PaymentService
from providers.stripe_provider import Stripe
from pricing.base_calculator import BaseCalculator
from services.event_dispatcher import EventDispatcher

# Setup
provider = Stripe()
calculator = BaseCalculator()
dispatcher = EventDispatcher()

# Create service
service = PaymentService(provider, calculator, dispatcher)

# Process payment
transaction_id = service.pay(user_id='123', base_price=100.0)
```

### Advanced Example with Tax and Discount

```python
from pricing.base_calculator import BaseCalculator
from pricing.tax_calculator import TaxCalculator
from pricing.discount_calculator import DiscountCalculator

# Compose calculators: apply discount first, then tax
calculator = BaseCalculator()
calculator = DiscountCalculator(calculator, discount_rate=0.15)  # 15% discount
calculator = TaxCalculator(calculator, tax_rate=0.1)  # 10% tax

service = PaymentService(provider, calculator, dispatcher)
transaction_id = service.pay(user_id='123', base_price=100.0)
```

### Adding Event Listeners

```python
from listeners.log_listener import LogListener
from listeners.admin_alert_listener import AdminAlertListener

dispatcher = EventDispatcher()
dispatcher.attach(LogListener())
dispatcher.attach(AdminAlertListener())
```

### Running the Application

```bash
uv run main.py
```

## Design Patterns

- **Strategy Pattern**: Different payment providers and price calculators can be swapped at runtime
- **Decorator Pattern**: Price calculators are composable (tax, discount can be stacked)
- **Observer Pattern**: Event listeners observe and react to payment events
- **Dependency Injection**: All dependencies are injected, making the system testable and flexible

## Extending the System

### Adding a New Payment Provider

1. Implement the `PaymentProvider` interface:

```python
from src.interfaces.payment_provider import PaymentProvider

class NewProvider(PaymentProvider):
    def charge(self, user_id: str, amount_cents: int) -> str:
        # Implementation here
        return "transaction_id"
```

2. Use it in your code:

```python
provider = NewProvider()
service = PaymentService(provider, calculator, dispatcher)
```

### Adding a New Price Calculator

1. Implement the `PriceCalculator` interface:

```python
from src.interfaces.price_calculator import PriceCalculator

class CustomCalculator(PriceCalculator):
    def calculate(self, price: float) -> float:
        # Your calculation logic
        return modified_price
```

2. Compose it with other calculators:

```python
calculator = BaseCalculator()
calculator = CustomCalculator(calculator)
```

### Adding a New Event Listener

1. Implement the `EventListener` interface:

```python
from src.interfaces.event_listener import EventListener

class CustomListener(EventListener):
    def update(self, event_data: dict):
        # Handle the event
        pass
```

2. Attach it to the dispatcher:

```python
dispatcher.attach(CustomListener())
```

## Testing

Run the test suite:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=. --cov-report=html
```

## Key Components

### PaymentService

The central service that orchestrates payment processing:
- Accepts a payment provider, price calculator, and event dispatcher
- Calculates final price using the calculator
- Processes payment through the provider
- Dispatches events for success/failure

### Payment Providers

- **StripeProvider**: Implements Stripe payment processing
- **PayPalProvider**: Implements PayPal payment processing

Both implement the `PaymentProvider` interface with a `charge()` method.

### Price Calculators

- **BaseCalculator**: Returns the base price unchanged
- **TaxCalculator**: Adds tax to the price
- **DiscountCalculator**: Applies a discount to the price

Calculators can be composed using the Decorator pattern.

### Event System

The system dispatches events for:
- `PAYMENT_SUCCESS`: Payment processed successfully
- `PAYMENT_FAILURE`: Payment processing failed
- `PAYMENT_ALERT`: Admin alerts for payment events

Listeners automatically receive notifications for these events.

