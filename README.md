# payment-system-maryia

- Create a unified interface that all payment providers must implement (e.g., a method like `charge(user_id: str, amount_cents: int) -> str)`.
- Simulate at least two different payment provider implementations (e.g., Stripe, PayPal), each relying on its own internal logic or SDK structure.
- Your system should work with any provider that conforms to the common interface, without changing core payment logic.


Implement Modular Price Calculation Logic:

- Separate price computation from the main payment processing flow.

- Support dynamic price modifications such as applying tax or discounts based on configuration or external input.

- Design your calculation logic in a way that allows it to be easily replaced or extended without modifying the payment service itself.



**Build a Composable Payment Service:**
- Create a central service that handles the payment process by combining the payment provider and pricing logic.
- The service should not be tightly coupled to specific provider or pricing implementations. You should be able to plug in different implementations as needed.
- Make sure dependencies are injected from outside and not hardcoded inside the class.