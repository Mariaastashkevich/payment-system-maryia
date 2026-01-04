from src.interfaces.payment_provider import PaymentProvider
import uuid


class Stripe(PaymentProvider):
    def charge(self, user_id: str, amount_cents: int) -> str:
        print(f"Stripe charge for user {user_id}: {amount_cents}")
        transaction_id = str(uuid.uuid4())
        return transaction_id