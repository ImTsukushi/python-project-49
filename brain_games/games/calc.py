from random import randint
from random import choice

TASK = 'What is the result of the expression?'


def get_game_data():
    first_int_for_question = randint(1, 50)
    second_int_for_question = randint(1, 50)
    operation_for_question = choice(['+', '-', '*'])
    print(
        f'Question: {first_int_for_question} {operation_for_question} '
        f'{second_int_for_question}'
    )
    correct_answer = eval(f'{first_int_for_question}'
                          f'{operation_for_question}'
                          f'{second_int_for_question}'
                          )
    return correct_answer
