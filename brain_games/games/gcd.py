from random import randint
from math import gcd

TASK = 'Find the greatest common divisor of given numbers.'


def get_game_data():
    first_int_for_question = randint(1, 50)
    second_int_for_question = randint(1, 50)
    print(f'Question: {first_int_for_question} {second_int_for_question}')
    correct_answer = gcd(first_int_for_question, second_int_for_question)
    return correct_answer
