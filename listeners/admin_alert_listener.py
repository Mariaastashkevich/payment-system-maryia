import logging
from src.interfaces.event_listener import EventListener
from src.events.event_type import EventType

logger = logging.getLogger(__name__)


class AdminAlertListener(EventListener):
    def update(self, event_data):
        try:
            match event_data.get('type'):
                case EventType.PAYMENT_ALERT.value | EventType.PAYMENT_FAILURE.value:
                    logger.error(f"ADMIN ALERT: user {event_data.get('user_id', 'unknown')}")
                case _:
                    pass
        except (TypeError, AttributeError) as e:
            logger.warning(f"Failed to parse event data: {e}")