from random import randint

TASK = 'What number is missing in the progression?'
LENGTH = 10
MIN_FIRST_NUMBER = 1
MAX_FIRST_NUMBER = 20
MIN_PROGRESSION_STEP = 2
MAX_PROGRESSION_STEP = 5
MIN_HIDDEN_INDEX = 0
MAX_HIDDEN_INDEX = 9


# Создаем прогрессию длинной 10 чисел
def make_progression(first_number, progression_step):
    progression = []
    for i in range(LENGTH):
        progression.append(str(first_number))
        first_number += progression_step
    return progression


# Скрываем правильный ответ в прогрессии
def make_hidden_number(progression):
    hidden_index = randint(MIN_HIDDEN_INDEX, MAX_HIDDEN_INDEX)
    hidden_number = progression[hidden_index]
    progression[hidden_index] = '..'
    return hidden_number, progression


# Генерируем числа, создаем вопрос, вычисляем правильный ответ
def get_game_data():
    first_number = randint(MIN_FIRST_NUMBER, MAX_FIRST_NUMBER)
    progression_step = randint(MIN_PROGRESSION_STEP, MAX_PROGRESSION_STEP)
    progression = make_progression(first_number, progression_step)
    hidden_number, progression = make_hidden_number(progression)
    correct_answer = hidden_number
    question = ' '.join(progression)
    return correct_answer, question
