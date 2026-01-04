import logging
from src.events.event_type import EventType
from src.interfaces.event_listener import EventListener

logger = logging.getLogger(__name__)


class LogListener(EventListener):
    def update(self, event_data):
        """
        Handles payment events and logs their result
        event_data: {'type': 'payment_success', 'user_id': "12", 'amount': 1000}
        """
        try:
            match event_data.get('type'):
                case EventType.PAYMENT_SUCCESS.value:
                    logger.info(f"Payment success received for user {event_data.get('user_id', 'unknown')} : {event_data.get('amount', 0)}")
                case EventType.PAYMENT_FAILURE.value:
                    logger.info(f"Payment failed for user: {event_data.get('user_id', 'unknown')} !")
                case _:
                    logger.error(f"Unknown event type {event_data.get('type')}")
        except TypeError as e:
            logger.warning(f"Failed to parse event data: {e}")
