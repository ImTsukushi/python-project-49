from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 50


# Узнаем простое ли число
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


# Игра
def get_game_data():
    question = randint(MIN_NUMBER, MAX_NUMBER)
    if not is_prime(question):
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    return correct_answer, question
