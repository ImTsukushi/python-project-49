from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game_data():
    question = randint(1, 50)
    correct_answer = question % 2 == 0
    return correct_answer, question
