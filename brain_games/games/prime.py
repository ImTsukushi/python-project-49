from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_game_data():
    int_for_question = randint(1, 50)
    print(f'Question: {int_for_question}')
    # Узнаем простое ли число
    if int_for_question == 1:
        correct_answer = 'no'
        return correct_answer
    for i in range(2, int(int_for_question ** 0.5) + 1):
        if int_for_question % i == 0:
            correct_answer = 'no'
            return correct_answer
    correct_answer = 'yes'
    return correct_answer
