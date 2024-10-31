from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: str) -> str:
    """ Функция, которая маскирует номер счета или карты"""
    parts = type_and_number.split() # разбиваем строку на части
    text_result = " ".join(parts[:-1]) # определяем тип карты или счет
    digit_result = parts[-1] # получаем номер карты/счета
    digit_count = len(digit_result)
    if digit_count > 16:
        return f"{text_result.strip()} {get_mask_account(digit_result)}"
    else:
        return f"{text_result.strip()} {get_mask_card_number(digit_result)}"


print(mask_account_card("Visa Platinum 7000792289606361"))


def get_date(data_time: str) -> str:
    """Функция, которая изменяет формат даты"""
    data_time_new = data_time[:10]
    year, month, day = data_time_new.split("-")
    return f"{day}.{month}.{year}"


data_input = get_date("2024-03-11T02:26:18.671407")
print(data_input)

