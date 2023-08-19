import prompt
from random import randint


# Приветственное сообщение, запрашиваем имя, выводим условие игры,
# назначаем счет
def welcome_gamer(task):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(task)
    score = 0
    return name, score


# Запрашиваем ответ, сравниваем его с корректным ответом и начисляем очки
def is_correct_answer(correct_answer, score):
    answer = prompt.string('Your answer: ')
    if answer == str(correct_answer):
        score += 1
        print('Correct!')
        return score
    else:
        print(
            f"'{answer}' is wrong answer ;(. "
            f"Correct answer was '{correct_answer}'."
        )
        exit()


# Поздравительное сообщение, если набрано 3 очка
def end_of_game(score, name):
    if score == 3:
        print(f'Congratulations {name}!')
        exit()


# Создаем случайную прогрессию длинной 10 символов
def random_progression():
    first_number = randint(1, 20)
    progression_step = randint(2, 5)
    hidden_number = randint(0, 9)
    progression = []
    for i in range(10):
        progression.append(str(first_number))
        first_number += progression_step
    correct_answer = progression[hidden_number]
    progression[hidden_number] = '..'
    progression = ' '.join(progression)
    return progression, correct_answer


# Проверка на простое число
def is_prime(number):
    if number == 1:
        return 'no'
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return 'no'
    return 'yes'
