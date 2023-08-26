import prompt

SCORE_TO_WIN = 3


def brain_main(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.TASK)
    for i in range(SCORE_TO_WIN):
        correct_answer, question = game.get_game_data()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {name}!"
            )
            exit()
    print(f'Congratulations, {name}!')
    exit()
