from os.path import isfile
import json
import random
from typing import List, Tuple

QUESTION_FILE_PATH = "questions.json"


def get_questions(file: str) -> List[dict]:
    """
    Функция для извлечения словарея с
    вопросами из JSON формата.
    """
    if isfile(file):
        with open(file) as f:
            return json.load(f)
    else:
        print("Файл не найден")
        return []


# в данной функции присутствует цикл Wile, который лучше заменить на цикл for,
# тем самым можно сократить код убрав лишнюю переменную question_quantity и лишние операции с ней
# отсутствует типизация, присутствуют избыточные комментарии
# def start_game(question):
#     """
#     Функция с основным кодом игры
#     :param question: в данный параметр мы получаем список со словарями вопросов
#     :return: возвращаем статистику правильных ответов и количество заданных вопросов
#     """
#     # Создаем переменную в которой хранится общее количество вопросов.
#     question_quantity = len(question)
#     # Создаем переменную для подсчета статистики правильных ответов.
#     statistic = 0
#     # Создаем переменную для сохранения общего количества вопросов.
#     question_number = 1
#
#     while question_quantity != 0:
#
#         random.shuffle(question)
#         question1 = question[0]
#
#         # Задаем вопрос с помощью метода build_question
#         print(question1.build_question(question_number))
#         # Проверяем корректность ответа пользователя методом is_correct
#         if question1.is_correct(str(input())):
#             print(f'Молодец, получено {question1.get_points()} баллов')
#             question_quantity -= 1
#             statistic += 1
#             question_number += 1
#         else:
#             print(f'Ответ неверный. Верный ответ – {question1.correct_answer[0]}')
#             question_quantity -= 1
#             question_number += 1
#     # Возвращаем данные для дальнейшей обработки статистики
#     return statistic, question_number

# Решение
def start_game(questions: list) -> Tuple[int, int]:
    """
    Функция с основным кодом игры
    :param questions: в данный параметр мы получаем список со словарями вопросов
    return: возвращаем статистику правильных ответов и количество заданных вопросов
    """

    statistic: int = 0
    question_number: int = 1

    random.shuffle(questions)

    for question in questions:
        print(question.build_question(question_number))

        if question.is_correct(str(input())):
            print(f'Молодец, получено {question.get_points()} баллов')
            statistic += 1
            question_number += 1
        else:
            print(f'Ответ неверный. Верный ответ – {question.correct_answer[0]}')
            question_number += 1

    return statistic, question_number


def get_result(statistic: int, question_number: int) -> None:
    """
    Функция для вывода финальной статистики
    :param statistic: показывает количество правильных ответов
    :param question_number: показывает общее число заданных вопросов
    """

    print("Вот и все")
    print(f'Отвечено {statistic} вопросов из {question_number - 1}')
