from random import randint
from brain_games import welcome_gamer
from brain_games import is_correct_answer
from brain_games import end_of_game


def brain_even():
    TASK = 'Answer "yes" if the nuber is even, otherwise answer "no".'
    name, score = welcome_gamer(TASK)
    while score < 3:
        int_for_question = randint(1, 50)
        print(f'Question: {int_for_question}')
        correct_answer = 'yes' if int_for_question % 2 == 0 else 'no'
        score = is_correct_answer(correct_answer, score)
    end_of_game(score, name)
