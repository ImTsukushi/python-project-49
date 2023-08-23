import prompt


def brain_main(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.TASK)
    score = 0
    while score < 3:
        correct_answer, question = game.get_game_data()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if type(correct_answer) == bool:
            if not correct_answer:
                correct_answer = 'no'
            else:
                correct_answer = 'yes'
        if answer == str(correct_answer):
            score += 1
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {name}!"
            )
            exit()
    if score == 3:
        print(f'Congratulations, {name}!')
        exit()
