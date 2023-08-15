#!/usr/bin/env python3
from random import randint
import prompt
import brain_games


def is_even(number):
    return number % 2 == 0


def brain_even():
    name = brain_games.welcome_user()
    print('Answer "yes" if the nuber is even, otherwise answer "no".')
    score = 0
    while score < 3:
        int_for_question = randint(1, 50)
        print(f'Question: {int_for_question}')
        answer = prompt.string('Your answer: ')
        correct_answer = 'yes' if is_even(int_for_question) else 'no'
        if answer == correct_answer:
            score += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was {correct_answer}.")
            exit()
    print(f'Congratulations {name}!')
    exit()


def main():
    brain_even()


if __name__ == '__main__':
    main()
