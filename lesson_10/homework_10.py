"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging
import logging.config
import json
import os

def setup_logging(config_path):
    """
    Налаштовує логування на основі конфігурації з JSON-файлу.

    config_path: Шлях до файлу конфігурації логування.
    """
    # Перевірка та створення каталогу для логів, якщо він не існує
    log_dir = os.path.join(os.path.dirname(config_path), 'logs')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Завантаження конфігурації логування з JSON
    with open(config_path, 'r') as file:
        config = json.load(file)
        logging.config.dictConfig(config)

# Викликаємо налаштування логування, вказуючи шлях до файлу конфігурації
setup_logging(r'C:\Project\AQA\lesson_10\logger_config.json')


def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:
    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення логера
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)

# Виклики функції для перевірки логування
if __name__ == "__main__":
    log_event("test_user", "success")
    log_event("test_user", "expired")
    log_event("test_user", "failed")
