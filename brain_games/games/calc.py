from random import randint
from random import choice

TASK = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 50


def get_game_data():
    first_int_for_question = randint(MIN_NUMBER, MAX_NUMBER)
    second_int_for_question = randint(MIN_NUMBER, MAX_NUMBER)
    operation_for_question = choice(['+', '-', '*'])
    correct_answer = eval(f'{first_int_for_question}'
                          f'{operation_for_question}'
                          f'{second_int_for_question}'
                          )
    question = (f'{first_int_for_question} {operation_for_question} '
                f'{second_int_for_question}')
    return correct_answer, question
