from random import randint
from math import gcd

TASK = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 50


def get_game_data():
    first_int_for_question = randint(MIN_NUMBER, MAX_NUMBER)
    second_int_for_question = randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{first_int_for_question} {second_int_for_question}'
    correct_answer = gcd(first_int_for_question, second_int_for_question)
    return correct_answer, question
