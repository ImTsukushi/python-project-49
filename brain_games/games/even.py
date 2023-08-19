from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game_data():
    int_for_question = randint(1, 50)
    print(f'Question: {int_for_question}')
    correct_answer = 'yes' if int_for_question % 2 == 0 else 'no'
    return correct_answer
