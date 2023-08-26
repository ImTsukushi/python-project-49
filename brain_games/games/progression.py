from random import randint

TASK = 'What number is missing in the progression?'
NUM_VALUES_IN_PROGRESSION = 10
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


# Создаем прогрессию длинной 10 чисел
def make_progression_list(first_number, progression_step):
    progression = []
    for i in range(NUM_VALUES_IN_PROGRESSION):
        progression.append(str(first_number))
        first_number += progression_step
    return progression


# Вычисляем правильный ответ
def get_game_data():
    first_number, progression_step, hidden_number = create_progression_data()
    progression = make_progression_list(first_number, progression_step)
    correct_answer = progression[hidden_number]
    progression[hidden_number] = '..'
    question = ' '.join(progression)
    return correct_answer, question

