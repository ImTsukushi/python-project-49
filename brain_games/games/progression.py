import prompt
from brain_games import welcome_user
from brain_games import is_correct_answer
from brain_games import end_of_game
from brain_games import random_progression


def brain_progression():
    task = 'What number is missing in the progression?'
    name, score = welcome_user(task)
    while score < 3:
        progression, correct_answer = random_progression()
        print(f'Question: {progression}')
        answer = prompt.string('Your answer: ')
        score = is_correct_answer(answer, correct_answer, score)
    end_of_game(score, name)
