def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, формирующая данные по указанному параметру транзакции"""
    return [el for el in list_dict if el["state"] == state]


def sort_by_date(list_dict: list[dict], date_sort: bool = True) -> list[dict]:
    """Функция, сортирующая транзакции по дате."""
    for item in list_dict:
        date = item.get("date")
        # Проверяем, что дата является строкой and соответствует формату ISO 8601
        if not isinstance(date, str) or len(date) < 19 or date[10] != 'T':
            raise ValueError(f"Некорректный формат даты: {date}")

    sorted_date = sorted(list_dict, key=lambda x: x["date"], reverse=date_sort)
    return sorted_date
