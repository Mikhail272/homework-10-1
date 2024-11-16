import pytest
from src.widget import (
    mask_account_card,
    get_mask_account,
    get_mask_card_number,
    get_date,
)


@pytest.fixture
def expected_masked_cards():
    return [
        ("Visa 7000792289606361", "Visa 7000 79** **** 6361"),  # Корректная карта
        (
            "MasterCard 1234567812345678",
            "MasterCard 1234 56** **** 5678",
        ),  # Корректная карта
        ("Bank Account 1234567890123456789", "Bank Account **6789"),  # Корректный счет
    ]


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        ("Visa 7000792289606361", "Visa 7000 79** **** 6361"),
        ("MasterCard 1234567812345678", "MasterCard 1234 56** **** 5678"),
        ("Bank Account 1234567890123456789", "Bank Account **6789"),
        ("Savings Account 11112222333344445555", "Savings Account **5555"),
    ],
)
def test_mask_account_card(input_data, expected_output):
    assert mask_account_card(input_data) == expected_output


@pytest.mark.parametrize(
    "invalid_input", ["InvalidInput", "", "Visa", "MasterCard 123"]
)
def test_mask_account_card_invalid(invalid_input):
    with pytest.raises(ValueError):  # Возникает ошибка в случае некорректного ввода
        mask_account_card(invalid_input)


@pytest.mark.parametrize(
    "account_number,expected_output",
    [
        ("73654108430135874305", "**4305"),
        ("788", "Неверный формат номера счета"),
    ],
)
def test_get_mask_account(account_number, expected_output):
    assert get_mask_account(account_number) == expected_output


@pytest.mark.parametrize(
    "card_number,expected_output",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("800079228960636", "Неверный формат банковской карты"),
    ],
)
def test_get_mask_card_number(card_number, expected_output):
    assert get_mask_card_number(card_number) == expected_output


def test_get_date():
    data_input = "2024-03-11T02:26:18.671407"
    assert get_date(data_input) == "11.03.2024"  # получение корректного результата


@pytest.mark.parametrize(
    "invalid_input",
    [
        "InvalidInput",  # Некорректный ввод
        "",  # Пустая строка
    ],
)
def test_get_date_invalid(invalid_input):
    with pytest.raises(ValueError):  # Проверяем, что возникает ошибка
        get_date(invalid_input)
