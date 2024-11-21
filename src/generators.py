def filter_by_currency(transactions, currency_code):
    """Фильтрует транзакции по заданной валюте и возвращает итератор."""
    for transaction in transactions:
        # Проверяем, соответствует ли валюта заданной
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield transaction


# переместите переменную transactions сюда или передавайте её в функции
def get_usd_transactions(transactions):
    """Возвращает итератор транзакций в USD."""
    return filter_by_currency(transactions, "USD")


def transaction_descriptions(transactions):
    """Генератор, который возвращает описания транзакций по очереди."""
    for transaction in transactions:
        yield transaction.get("description", "")



if __name__ == "__main__":
    transactions = []
    # Получаем итератор транзакций в USD
    usd_transactions = get_usd_transactions(transactions)


    try:
        for _ in range(2):
            print(next(usd_transactions))
    except StopIteration:
        print("Нет доступных транзакций в USD.")

    # Получаем генератор описаний транзакций
    descriptions = transaction_descriptions(transactions)
    try:
        for _ in range(5):
            print(next(descriptions))
    except StopIteration:
        print("Нет описаний транзакций.")


def card_number_generator(start, end):
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX."""
    for num in range(start, end + 1):
        # Преобразование числа в строку с добавлением нулей слева, если необходимо
        card_number = f"{num:016d}"  # Форматируем число как 16-значное с ведущими нулями
        # Форматируем номер карты в виде XXXX XXXX XXXX XXXX
        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_card_number



if __name__ == "__main__":
    for card_number in card_number_generator(1, 5):
        print(card_number)