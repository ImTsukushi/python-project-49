from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_game_data():
    question = randint(2, 50)
    # Узнаем простое ли число
    for i in range(2, int(question ** 0.5) + 1):
        if question % i == 0:
            return False, question
    return True, question
