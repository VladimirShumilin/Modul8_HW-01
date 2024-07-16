"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count

def randomized_binary_search(number:int=1, start:int = 1, end:int = 101) -> int:
    """Угадываем число используя модифицированный алгоритм бинарного поиска

    Args:
        number (int, optional): Загаданное число. Defaults to 1.
        start (int, optional): Начальная граница диапазона поиска. Defaults to 1.
        end (int, optional): Конечная граница диапазона поиска. Defaults to 101.
    Returns:
        int: Число попыток
    """
    
    count = 0
    
    while start <= end:
        count += 1
        
        # если start и end равны считаем что это и есть середина диапазона и угадываем число
        # иначе генерим случайное число внутри текущего диапазона
        if start == end:
            mid = start
        else:
            mid = np.random.randint(start, end)

        if mid == number:
            return count  # выход из цикла, если угадали
        elif mid > number:
            end = mid - 1 # уменьшаем конечную границу
        else:
            start = mid + 1 # увеличиваем начальную границу
            
    return None

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
    score_game(randomized_binary_search)
