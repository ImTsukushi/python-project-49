import prompt


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