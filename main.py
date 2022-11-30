"""
Лабораторная работа #10
Выполнил Прокофьев А.А. Фт-210008
"""

def calc_count(currency, banknote_cost):
    """
    Подсчитать сколько купюр данного достоинства может быть в указанном количестве
    """

    return currency // banknote_cost, currency % banknote_cost


def get_currency_count(currency):
    """
    Подсчитать сколько в минимуме надо банкнот чтобы собрать число currency
    """

    change = currency
    response = dict()

    for i in range(6, -1, -1):
        banknote_cost = 2 ** i
        count, change = calc_count(change, banknote_cost)

        if count != 0:
            response[banknote_cost] = count

    return response


def main():
    """
    Главная функция программы
    """

    n_value = int(input("Введите N >> "))
    response = get_currency_count(n_value)

    print("Результаты:")
    print(f"Для того, чтобы собрать сумму N={n_value}, вам надо: ")

    for key, value in response.items():
        print(f"\t·купюры достоинством в {key} в количестве {value} штук;")


if __name__ == "__main__":
    main()
