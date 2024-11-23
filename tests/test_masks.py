import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("800079228960636") == "Неверный формат банковской карты"
    assert get_mask_card_number("123") == "Неверный формат банковской карты"
    assert (
        get_mask_card_number("abcdefghabcdefgh") == "Неверный формат банковской карты"
    )
    assert get_mask_card_number("") == "Неверный формат банковской карты"


@pytest.mark.parametrize("x", [7000792289606361, 8000522289606361, 7000792289606361])
def test_get_mask_card_number_parametrized(x):
    card_number_str = str(x)
    expected_masked = (
        f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
    )
    assert get_mask_card_number(card_number_str) == expected_masked


def test_get_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("788") == "Неверный формат номера счета"
    assert get_mask_account("") == "Неверный формат номера счета"


@pytest.mark.parametrize(
    "x", [73654108430135874305, 773654108430135874305, 3373654108430135874305]
)
def test_get_mask_account_parametrized(x):
    account_number_str = str(x)
    assert get_mask_account(account_number_str) == f"**{account_number_str[-4:]}"
