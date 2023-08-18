from brain_games import welcome_gamer
from brain_games import is_correct_answer
from brain_games import end_of_game
from brain_games import random_progression


def brain_progression():
    task = 'What number is missing in the progression?'
    name, score = welcome_gamer(task)
    while score < 3:
        progression, correct_answer = random_progression()
        print(f'Question: {progression}')
        score = is_correct_answer(correct_answer, score)
    end_of_game(score, name)
