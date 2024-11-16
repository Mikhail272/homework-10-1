import pytest

from conftest import test_state
from src.processing import filter_by_state, sort_by_date


# Тестирование на корректную работу функции сортировки по статусу транзакции
def test_filter_by_state(test_state):
    expected_output = [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
                       ]

    result = filter_by_state(test_state, "CANCELED")
    assert result == expected_output

@pytest.mark.parametrize("state, expected_output", [
    ('EXECUTED', [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
                  ]), # Ожидаемый результат для "EXECUTED"
    ('CANCELED', [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
                  ]), # Ожидаемый результат для "CANCELED"
    ('not_found', []) # Ожидаемый результат для состояния, которое не существует в данных
    ])

def test_filter_by_state(test_state, state, expected_output):
    result = filter_by_state(test_state, state)
    assert result == expected_output


# Тестирование на корректную работу функции сортировки по дате транзакции
@pytest.mark.parametrize("date_sort, expected_output", [(True, [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
        ]),
        (False, [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
        ])
    ])

def test_sort_by_date(test_state, date_sort, expected_output):
    result = sort_by_date(test_state, date_sort=date_sort)
    assert result == expected_output


def test_sort_by_date_with_same_dates():
    """Тест на обработку идентичных дат."""
    test_data = [
        {'id': 1, 'state': 'EXECUTED', 'date': '2022-01-01T00:00:00'},
        {'id': 2, 'state': 'EXECUTED', 'date': '2022-01-01T00:00:00'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2022-01-01T00:00:00'}
    ]

    expected_output = test_data.copy()  # Ожидается, что порядок сохранится
    result = sort_by_date(test_data, date_sort=True)
    assert result == expected_output


def test_sort_by_date_with_invalid_dates():
    """Тест на обработку некорректных форматов дат."""
    test_data = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': 'invalid-date'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]

    with pytest.raises(ValueError):
        sort_by_date(test_data)


def test_sort_by_date_with_non_standard_date_format():
    """Тест на обработку нестандартного формата даты."""
    test_data = [
        {'id': 1, 'state': 'EXECUTED', 'date': '01/01/2022 00:00:00'},
        {'id': 2, 'state': 'EXECUTED', 'date': '2022-01-02T00:00:00'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2022-01-01T00:00:00'}
    ]

    # Если формат даты не поддерживается, вызов должен привести к исключению
    with pytest.raises(ValueError):
        sort_by_date(test_data)
