import pytest

@pytest.fixture
def test_state():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# Фикстура для создания общего списка транзакций

@pytest.fixture
def test_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 842164879,
            "state": "EXECUTED",
            "date": "2020-07-01T17:15:50.202103",
            "operationAmount": {
                "amount": "5000.00",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 99999999999999999999",
            "to": "Счет 11111111111111111111"
        },
        {
            "id": 103845286,
            "state": "EXECUTED",
            "date": "2021-01-15T12:34:56.789012",
            "operationAmount": {
                "amount": "1500.00",
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Карта 1234567890123456",
            "to": "Карта 6543210987654321"
        },
        {
            "id": 765432143,
            "state": "EXECUTED",
            "date": "2021-03-05T14:22:33.987654",
            "operationAmount": {
                "amount": "30000.00",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 11122233344455566677",
            "to": "Счет 77788899900011122223"
        }
    ]


