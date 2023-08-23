from random import randint

TASK = 'What number is missing in the progression?'


def get_game_data():
    first_number = randint(1, 20)
    progression_step = randint(2, 5)
    hidden_number = randint(0, 9)
    progression = []
    # Создаем прогрессию длинной 10 чисел
    for i in range(10):
        progression.append(str(first_number))
        first_number += progression_step
    correct_answer = progression[hidden_number]
    progression[hidden_number] = '..'
    question = ' '.join(progression)
    return correct_answer, question
