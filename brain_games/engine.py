import prompt


def brain_main(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.TASK)
    score = 0
    while score < 3:
        correct_answer = game.get_game_data()
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            score += 1
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            exit()
    if score == 3:
        print(f'Congratulations {name}!')
        exit()
