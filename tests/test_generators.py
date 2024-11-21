import pytest
from src.generators import filter_by_currency, get_usd_transactions, transaction_descriptions, card_number_generator

# Тестирование функции filter_by_currency
@pytest.mark.parametrize(
    "currency_code, expected_ids",
    [
        ("USD", [939719570, 142264268, 765432143]),  # Ожидаем транзакции с валютой USD
        ("EUR", [842164879]),  # Ожидаем транзакцию с валютой EUR
        ("RUB", []),  # Нет транзакций с валютой RUB
        ("GBP", []),  # Нет транзакций с валютой GBP
        (None, []),  # Проверка на отсутствие валюты в транзакциях
    ]
)
def test_filter_by_currency(test_transactions, currency_code, expected_ids):
    result = list(filter_by_currency(test_transactions, currency_code))
    result_ids = [transaction["id"] for transaction in result]
    assert result_ids == expected_ids


# Тестирование функции get_usd_transactions
def test_get_usd_transactions(test_transactions):
    # Проверяем, что вернется только транзакции с валютой USD
    usd_transactions = get_usd_transactions(test_transactions)
    result_ids = [transaction["id"] for transaction in usd_transactions]
    assert result_ids == [939719570, 142264268, 765432143]

    # Проверяем случай, когда транзакции не содержат валюты USD
    no_usd_transactions = get_usd_transactions([])
    assert list(no_usd_transactions) == []  # Ожидаем пустой список


# Тестирование функции transaction_descriptions
def test_transaction_descriptions(test_transactions):
    descriptions = list(transaction_descriptions(test_transactions))
    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод организации",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert descriptions == expected_descriptions

    # Тестируем случай с пустыми транзакциями
    empty_transactions = []
    empty_descriptions = list(transaction_descriptions(empty_transactions))
    assert empty_descriptions == []  # Ожидаем пустой список

    # Тестируем случай, когда у транзакций нет описания
    transactions_no_description = [
        {"id": 1, "state": "EXECUTED", "date": "2020-01-01", "description": ""},
        {"id": 2, "state": "EXECUTED", "date": "2020-01-02", "description": None}
    ]
    descriptions = list(transaction_descriptions(transactions_no_description))
    assert descriptions == ["", ""]  # Ожидаем пустые строки


# Тестирование генератора card_number_generator
@pytest.mark.parametrize(
    "start, end, expected_card_numbers",
    [
        (1, 5, [
            "0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003",
            "0000 0000 0000 0004",
            "0000 0000 0000 0005"
        ]),
        (1000, 1002, [
            "0000 0000 0000 1000",
            "0000 0000 0000 1001",
            "0000 0000 0000 1002"
        ]),
        (5000, 5000, ["0000 0000 0000 5000"]),  # Только один номер
        (0, 0, ["0000 0000 0000 0000"]),  # Номер карты 0000 0000 0000 0000
        (10, 9, []),  # Проверка на пустой диапазон
    ]
)
def test_card_number_generator(start, end, expected_card_numbers):
    result = list(card_number_generator(start, end))
    assert result == expected_card_numbers


# Тест для проверки обработки пустого списка транзакций
def test_get_usd_transactions_empty_list():
    transactions = []
    usd_transactions = get_usd_transactions(transactions)

    # Проверяем, что генератор не выдает транзакций
    with pytest.raises(StopIteration):
        next(usd_transactions)


def test_transaction_descriptions_empty_list():
    input_transactions = []
    descriptions = transaction_descriptions(input_transactions)

    # Проверяем, что генератор не выдает описаний
    with pytest.raises(StopIteration):
        next(descriptions)

# Дополнительные тесты для работы с пустыми данными и генераторами

# Тест проверки, что print выводит сообщение, если нет доступных транзакций
def test_print_no_usd_transactions(capfd):
    transactions = []  # Пустой список
    usd_transactions = get_usd_transactions(transactions)

    # Пробуем получить транзакции и захватываем вывод
    try:
        print(next(usd_transactions))
    except StopIteration:
        print("Нет доступных транзакций в USD.")

    # Проверяем, что вывод соответствует ожиданиям
    captured = capfd.readouterr()
    assert captured.out.strip() == "Нет доступных транзакций в USD."


# Тест проверки, что print выводит сообщение об отсутствии описаний
def test_print_no_descriptions(capfd):
    input_transactions = []  # Пустой список
    descriptions = transaction_descriptions(input_transactions)

    # Пробуем получить описания и захватываем вывод
    try:
        print(next(descriptions))
    except StopIteration:
        print("Нет описаний транзакций.")

    # Проверяем, что вывод соответствует ожиданиям
    captured = capfd.readouterr()
    assert captured.out.strip() == "Нет описаний транзакций."


if __name__ == "__main__":
    pytest.main()
