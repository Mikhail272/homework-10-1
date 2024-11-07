def filter_by_state(list_dict: list[dict], state="EXECUTED") -> list[dict]:
    """Функция, формирующая данные по указанному параметру транзакции"""
    return [el for el in list_dict if el["state"] == state]


status_klient = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


# state = "CANCELED"
# print(filter_by_state(status_klient, state))


def sort_by_date(list_dict: list[dict], date_sort: bool = True) -> list[dict]:
    """Функция, сортирующая транзакции по дате"""
    sorted_date = sorted(list_dict, key=lambda x: x["date"], reverse=True)
    return sorted_date


print(sort_by_date(status_klient))
