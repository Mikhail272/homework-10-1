def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, формирующая данные по указанному параметру транзакции"""
    return [el for el in list_dict if el["state"] == state]


def sort_by_date(list_dict: list[dict], date_sort: bool = True) -> list[dict]:
    """Функция, сортирующая транзакции по дате."""
    sorted_date = sorted(list_dict, key=lambda x: x["date"], reverse=not date_sort)
    return sorted_date
