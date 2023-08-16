from random import randint
import prompt
from brain_games import welcome_user
from brain_games import is_correct_answer
from brain_games import end_of_game


def brain_even():
    task = 'Answer "yes" if the nuber is even, otherwise answer "no".'
    name, score = welcome_user(task)
    while score < 3:
        int_for_question = randint(1, 50)
        print(f'Question: {int_for_question}')
        answer = prompt.string('Your answer: ')
        correct_answer = 'yes' if int_for_question % 2 == 0 else 'no'
        score = is_correct_answer(answer, correct_answer, score)
    end_of_game(score, name)
