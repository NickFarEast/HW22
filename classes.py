# В данном коде присутствует запах длинного списка параметров, отсутствие типизации,

# Было
# class GenericQuestion:
#
#     def __init__(self, question_text, author, complexity, correct_answer, topic):
#         self.question_text = question_text
#         self.author = author
#         self.complexity = complexity
#         self.correct_answer = correct_answer
#         self.topic = topic
#         self.is_answer_asked = False
#         self.user_answer = None
#         self.point = None


# Решение


from dataclasses import dataclass, field
from typing import Optional


@dataclass
class GenericQuestion:
    question_text: str
    author: str
    complexity: int
    topic: str
    correct_answer: list = field(default_factory=list)
    user_answer: Optional[str] = None
    point: Optional[str] = None


class Question(GenericQuestion):

    def get_points(self):
        return int(self.complexity) * 10

    def is_correct(self, answer):
        return True if answer in self.correct_answer else False

    def build_question(self, count):
        return f'Вопрос {count}, Тема: {self.topic}, Сложность: {self.complexity}, {self.question_text}'

