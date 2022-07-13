def timer(call_count, start_sleep_time=1, factor=2, border_sleep_time=30):
    """Декоратор для повторного выполнения декорируемой функции через некоторое время."""
    def function(func):
        def inner(*args):
            t = 0
            print(f'Кол-во запусков = {call_count}')
            print('Начало работы')
            count = 1
            for i in range(call_count):
                if t < border_sleep_time:
                    t = start_sleep_time * factor ** i
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
