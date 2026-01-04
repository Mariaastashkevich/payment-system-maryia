from abc import ABC, abstractmethod

class PaymentProvider(ABC):
    @abstractmethod
    def charge(self, user_id: str, amount_cents: int) -> str:
        pass

