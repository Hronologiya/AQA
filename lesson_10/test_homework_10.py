import unittest
from unittest.mock import patch, MagicMock
import logging
from homework_10 import log_event


class TestLogEvent(unittest.TestCase):

    @patch('homework_10.logging.getLogger')
    def test_log_event_success(self, mock_get_logger):
        """Тест успішного входу (success)"""
        mock_logger = MagicMock()
        mock_get_logger.return_value = mock_logger

        # Виклик функції з успішним статусом
        log_event('test_user', 'success')

        # Перевірка, що викликався метод info з правильним повідомленням
        mock_logger.info.assert_called_once_with("Login event - Username: test_user, Status: success")

    @patch('homework_10.logging.getLogger')
    def test_log_event_expired(self, mock_get_logger):
        """Тест застарілого пароля (expired)"""
        mock_logger = MagicMock()
        mock_get_logger.return_value = mock_logger

        # Виклик функції з статусом expired
        log_event('test_user', 'expired')

        # Перевірка, що викликався метод warning з правильним повідомленням
        mock_logger.warning.assert_called_once_with("Login event - Username: test_user, Status: expired")

    @patch('homework_10.logging.getLogger')
    def test_log_event_failed(self, mock_get_logger):
        """Тест невдалого входу (failed)"""
        mock_logger = MagicMock()
        mock_get_logger.return_value = mock_logger

        # Виклик функції з невдалим статусом
        log_event('test_user', 'failed')

        # Перевірка, що викликався метод error з правильним повідомленням
        mock_logger.error.assert_called_once_with("Login event - Username: test_user, Status: failed")


if __name__ == "__main__":
    unittest.main()
