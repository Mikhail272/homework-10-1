import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

# Тестирование функции filter_by_currency с параметризацией
@pytest.mark.parametrize("currency, expected_ids", [
    ("USD", [1, 3]),
    ("EUR", [2]),
    ("JPY", []),
])
def test_filter_by_currency(transactions, currency, expected_ids):
    filtered_transactions = list(filter_by_currency(transactions, currency))
    assert [t["id"] for t in filtered_transactions] == expected_ids

# Тестирование функции transaction_descriptions с параметризацией
@pytest.mark.parametrize("input_transactions, expected_descriptions", [
    (
        [
            {"description": "Перевод организации"},
            {"description": "Перевод со счета на счет"},
            {"description": "Перевод с карты на карту"}
        ],
        ["Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту"]
    ),
    (
        [],
        []
    ),
])
def test_transaction_descriptions(input_transactions, expected_descriptions):
    descriptions = list(transaction_descriptions(input_transactions))
    assert descriptions == expected_descriptions

# Тестирование генератора card_number_generator с параметризацией
@pytest.mark.parametrize("start, end, expected_numbers", [
    (1, 5, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003", "0000 0000 0000 0004", "0000 0000 0000 0005"]),
    (9999, 10000, ["0000 0000 9999 9999", "0000 0001 0000 0000"]),
])
def test_card_number_generator(start, end, expected_numbers):
    generated_numbers = list(card_number_generator(start, end))
    assert generated_numbers == expected_numbers
    assert all(len(num.replace(" ", "")) == 16 for num in generated_numbers)  # Проверка корректного форматирования

if __name__ == "__main__":
    pytest.main()