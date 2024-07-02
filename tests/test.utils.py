from src.utils import get_transaction_amount_in_rubles
import unittest


def test_get_transaction_amount_in_rubles_usd(self, mock_get):
    """Проверяет, что сумма транзакции в USD конвертируется в рубли."""
    mock_get.return_value.json.return_value = {
        "rates": {
            "USD": 75.00,
        }
    }
    amount_in_rubles = get_transaction_amount_in_rubles(100.00, "USD")
    assert amount_in_rubles == 7500.00


def test_get_transaction_amount_in_rubles_eur(self, mock_get):
    """Проверяет, что сумма транзакции в EUR конвертируется в рубли."""
    mock_get.return_value.json.return_value = {
        "rates": {
            "EUR": 90.00,
        }
    }
    amount_in_rubles = get_transaction_amount_in_rubles(50.00, "EUR")
    assert amount_in_rubles == 4500.00


def test_get_transaction_amount_in_rubles_rub(self):
    """Проверяет, что сумма транзакции в RUB остается неизменной."""
    amount_in_rubles = get_transaction_amount_in_rubles(1000.00, "RUB")
    assert amount_in_rubles == 1000.00


def test_get_transaction_amount_in_rubles_unsupported_currency(self):
    """Проверяет, что для неподдерживаемой валюты выбрасывается исключение ValueError."""
    with self.assertRaises(ValueError):
        get_transaction_amount_in_rubles(100.00, "JPY")


if __name__ == "__main__":
    unittest.main()

