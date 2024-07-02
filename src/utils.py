import requests
from typing import Dict, Union, Optional
from unittest.mock import patch
import unittest
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

github_token = os.getenv('API')


def get_exchange_rate(currency: str) -> float:
    """
    Получает текущий курс валюты по API.

    Args:
        currency: Валюта, для которой нужно получить курс.

    Returns:
        Текущий курс валюты по отношению к рублю.
    """

    # Вы можете использовать любой API для конвертации валют.
    # В качестве примера возьмем API от exchangerate-api.com
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}"

    payload = {}
    headers = {
        "apikey": "WXhRnMECKLLjNfIvAcaJnSUZzYzudYQT"
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    ret = response.json()
    return ret["rates"]["RUB"]


print(get_exchange_rate("USD"))


def get_transaction_amount_in_rubles(amount: float, currency: str) -> float:
    """
    Получает сумму транзакции в рублях.

    Args:
        amount: Сумма транзакции.
        currency: Валюта транзакции.

    Returns:
        Сумма транзакции в рублях.
    """

    if currency == "RUB":
        return amount
    elif currency in ("USD", "EUR"):
        rate = get_exchange_rate(currency)
        return amount * rate
    else:
        raise ValueError(f"Неподдерживаемая валюта: {currency}")


# if __name__ == "__main__":
#     unittest.main()

