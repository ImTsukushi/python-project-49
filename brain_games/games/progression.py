from random import randint

TASK = 'What number is missing in the progression?'
LENGTH = 10
MIN_FIRST_NUMBER = 1
MAX_FIRST_NUMBER = 20
MIN_PROGRESSION_STEP = 2
MAX_PROGRESSION_STEP = 5
MIN_HIDDEN_INDEX = 0
MAX_HIDDEN_INDEX = 9


# Создаем числа для прогрессии
def create_progression_data():
    initial_value = randint(MIN_FIRST_NUMBER, MAX_FIRST_NUMBER)
    progression_step = randint(MIN_PROGRESSION_STEP, MAX_PROGRESSION_STEP)
    hidden_index = randint(MIN_HIDDEN_INDEX, MAX_HIDDEN_INDEX)
    return initial_value, progression_step, hidden_index


# Создаем прогрессию длинной 10 чисел, выбираем скрываемое число
def make_progression_list(first_number, progression_step, hidden_index):
    progression = []
    for i in range(LENGTH):
        progression.append(str(first_number))
        first_number += progression_step
    hidden_number = progression[hidden_index]
    progression[hidden_index] = '..'
    return progression, hidden_number


# Вычисляем правильный ответ
def get_game_data():
    first_number, progression_step, hidden_index = create_progression_data()
    progression, hidden_number = make_progression_list(
        first_number, progression_step, hidden_index
    )
    correct_answer = hidden_number
    question = ' '.join(progression)
    return correct_answer, question
