import prompt
from random import randint


def welcome_user(task):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(task)
    score = 0
    return name, score


def is_correct_answer(answer, correct_answer, score):
    if answer == str(correct_answer):
        score += 1
        print('Correct!')
        return score
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was {correct_answer}.")
        exit()


def end_of_game(score, name):
    if score == 3:
        print(f'Congratulations {name}!')
        exit()


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
