from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(type_and_number: str) -> str:
    """ Функция, которая маскирует номер счета или карты"""
    text_result = ""
    digit_result = ""
    digit_count = 0
    for el in type_and_number:
        if el.isalpha() or el.isspace():
            text_result += el
        elif el.isdigit():
            digit_result += el
            digit_count += 1
    if digit_count > 16:
        return f"{text_result.strip()} {get_mask_account(digit_result)}"
    else:
        return f"{text_result.strip()} {get_mask_card_number(digit_result)}"


print(mask_account_card("Visa Platinum 7000792289606361"))
