from random import randint
from brain_games import welcome_gamer
from brain_games import is_correct_answer
from brain_games import end_of_game
from brain_games import is_prime


def brain_prime():
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    name, score = welcome_gamer(task)
    while score < 3:
        int_for_question = randint(1, 50)
        print(f'Question: {int_for_question}')
        correct_answer = is_prime(int_for_question)
        score = is_correct_answer(correct_answer, score)
    end_of_game(score, name)
