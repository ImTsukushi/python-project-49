from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 50


# Проверка на четность
def is_even(number):
    return number % 2 == 0


# Игра
def get_game_data():
    question = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = "yes" if is_even(question) else "no"
    return correct_answer, question
