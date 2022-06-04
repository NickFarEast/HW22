# -*- coding: utf-8 -*-
# Проблема
# В данном коде отсутствовала архитектура проекта(все в одной файле main)
# Решение
# в проекте создана архитектура с файлами, в зависимости от функции кода

from classes import Question
from functions import get_questions, start_game, get_result
QUESTION_FILE_PATH = "questions.json"


if __name__ == '__main__':
    question_raw = get_questions(QUESTION_FILE_PATH)
    questions = []
    for question in question_raw:
        questions.append(Question(
            question_text=question["question_text"],
            author=question["author"],
            complexity=question["complexity"],
            correct_answer=question["correct_answer"],
            topic=question["topic"]
        ))

    statistic, question_number = start_game(questions)
    get_result(statistic, question_number)
