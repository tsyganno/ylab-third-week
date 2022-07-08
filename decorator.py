def cash(func):
    """Кэширует значение декорируемой функции. Если декорируемая функция будет вызвана повторно с теми же параметрами —
    декоратор возвращает сохранённый результат, не выполняя функцию."""
    dictionary = {}

    def inner(*args):
        if args not in dictionary:
            dictionary[args] = func(*args)
        return dictionary[args]
    return inner


@cash
def multiplier(number: int):
    return number * 2


if __name__ == '__main__':
    print(multiplier(2))
    print(multiplier(4))
    print(multiplier(2))
