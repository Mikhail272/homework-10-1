import pytest
from src.decorators import my_function, log


# Функция, которая выбрасывает исключение для тестирования
@log()
def faulty_function():
    raise ValueError("This is a test error")

def test_my_function_success(capsys):
    result = my_function(3, 4)  # Ожидается 7
    assert result == 7

    # Перехватываем вывод
    captured = capsys.readouterr()
    assert "ok. Result: 7" in captured.out
    assert "Finished execution of my_function." in captured.out

def test_my_function_failure(capsys):
    with pytest.raises(ValueError):
        faulty_function()  # Ожидается ValueError

    # Перехватываем вывод
    captured = capsys.readouterr()
    assert "error: This is a test error" in captured.out
    assert "Finished execution of faulty_function." in captured.out

def test_timings(capsys):
    my_function(1, 2)  # Для того, чтобы посмотреть логи времени
    captured = capsys.readouterr()
    assert "Time taken for my_function:" in captured.out