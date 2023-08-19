from random import randint
from random import choice
from brain_games import welcome_gamer
from brain_games import is_correct_answer
from brain_games import end_of_game


def brain_calc():
    TASK = 'What is the result of the expression?'
    name, score = welcome_gamer(TASK)
    while score < 3:
        first_int_for_question = randint(1, 50)
        second_int_for_question = randint(1, 50)
        operation_for_question = choice(['+', '-', '*'])
        print(
            f'Question: {first_int_for_question} {operation_for_question}'
            f'{second_int_for_question}'
        )
        correct_answer = eval(f'{first_int_for_question}'
                              f'{operation_for_question}'
                              f'{second_int_for_question}'
                              )
        score = is_correct_answer(correct_answer, score)
    end_of_game(score, name)
