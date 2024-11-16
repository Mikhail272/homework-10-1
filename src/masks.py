from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция формирует замаскированный номер карты"""
    card_number = str(card_number)  # Преобразуем в строку
    if len(card_number) != 16 or not card_number.isdigit():
        return "Неверный формат банковской карты"
    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return masked_number


def get_mask_account(mask_account: Union[str, int]) -> str:
    """Функция формирует замаскированный номер счета"""
    mask_account = str(mask_account)  # Преобразуем в строку
    if len(mask_account) < 4 or not mask_account.isdigit():
        return "Неверный формат номера счета"
    masked_account = f"**{mask_account[-4:]}"
    return masked_account
