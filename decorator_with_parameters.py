def timer(call_count, start_sleep_time=1, factor=4, border_sleep_time=20):
    """Декоратор для повторного выполнения декорируемой функции через некоторое время."""
    def function(func):
        def inner(*args):
            t = start_sleep_time
            print(f'Кол-во запусков = {call_count}')
            print('Начало работы')
            count = 1
            for _ in range(call_count):
                if t < border_sleep_time:
                    t = t * 2 ** factor
                    print(f'Запуск номер {count}. Ожидание: {t} секунд. Результат декорируемой функций = {func(*args)}')
                    count += 1
                else:
                    t = border_sleep_time
                    print(f'Запуск номер {count}. Ожидание: {t} секунд. Результат декорируемой функций = {func(*args)}')
                    count += 1
            print('Конец работы')
        return inner
    return function


@timer(3)
def multiplier(number: int):
    return number * 2


if __name__ == '__main__':
    multiplier(2)
