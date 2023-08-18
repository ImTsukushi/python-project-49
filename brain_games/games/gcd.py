from random import randint
from math import gcd
import prompt
from brain_games import welcome_user
from brain_games import is_correct_answer
from brain_games import end_of_game


def brain_gcd():
    task = 'Find the greatest common divisor of given numbers.'
    name, score = welcome_user(task)
    while score < 3:
        first_int_for_question = randint(1, 50)
        second_int_for_question = randint(1, 50)
        print(f'Question: {first_int_for_question} {second_int_for_question}')
        answer = prompt.string('Your answer: ')
        correct_answer = gcd(first_int_for_question, second_int_for_question)
        score = is_correct_answer(answer, correct_answer, score)
    end_of_game(score, name)
