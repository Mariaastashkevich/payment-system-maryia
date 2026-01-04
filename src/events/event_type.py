from enum import Enum


class EventType(Enum):
    PAYMENT_SUCCESS = 'payment_success'
    PAYMENT_FAILURE = 'payment_failed'
    PAYMENT_ALERT = 'payment_alert'