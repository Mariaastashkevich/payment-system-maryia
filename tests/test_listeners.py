import pytest

from listeners.log_listener import LogListener, logger
from listeners.admin_alert_listener import AdminAlertListener
from src.events.event_type import EventType

@pytest.fixture
def log_listener():
    return LogListener()


@pytest.fixture
def alert_listener():
    return AdminAlertListener()


def test_log_listener_success(mocker, log_listener):
    mock_logger = mocker.patch('listeners.log_listener.logger')

    event = {
        'type': EventType.PAYMENT_SUCCESS.value,
        'user_id': '12',
        'amount': 1000
    }

    log_listener.update(event)

    mock_logger.info.assert_called_once_with('Payment success received for user 12 : 1000')


def test_log_listener_failure(mocker, log_listener):
    mock_logger = mocker.patch('listeners.log_listener.logger')

    event = {
        'type': EventType.PAYMENT_FAILURE.value,
        'user_id': '11',
        'amount': 2000
    }

    log_listener.update(event)

    mock_logger.info.assert_called_once_with('Payment failed for user: 11 !')


def test_log_listener_unknown(mocker, log_listener):
    mock_logger = mocker.patch('listeners.log_listener.logger')
    event = {
        'type': EventType.PAYMENT_ALERT.value,
        'user_id': '11',
        'amount': 2000
    }
    log_listener.update(event)

    mock_logger.error.assert_called_once_with(f"Unknown event type {event['type']}")


def test_admin_alert_listener_alert(mocker, alert_listener):
    mock_logger = mocker.patch('listeners.admin_alert_listener.logger')

    event = {
            'type': EventType.PAYMENT_ALERT.value,
            'user_id': '13',
            'amount': 34567
        }

    alert_listener.update(event)

    mock_logger.error.assert_called_once_with('ADMIN ALERT: user 13')


def test_admin_alert_listener_pass(mocker, alert_listener):
    mock_logger = mocker.patch('listeners.admin_alert_listener.logger')

    event = {
        'type': EventType.PAYMENT_FAILURE.value,
        'user_id': '11',
        'amount': 2000
    }

    alert_listener.update(event)

    mock_logger.error.assert_not_called()
    mock_logger.warning.assert_not_called()


def test_admin_alert_listener_invalid(mocker, alert_listener):
    mock_logger = mocker.patch('listeners.admin_alert_listener.logger')

    alert_listener.update(None)

    mock_logger.warning.assert_called_once()

