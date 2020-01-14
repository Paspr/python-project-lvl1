from brain_games.cli import run, prompt

NUMBER_OF_ROUNDS = 3


def greeting():
    print('Welcome to the Brain Games!')


def failure(wrong, right, player_name):
    print(f'"{wrong}" is a wrong answer ;(. Correct answer was "{right}"')
    print(f"Let's try again, {player_name}!")


def success(player_name):
    print(f"Congratulations, {player_name}!")


def run_game(game_name):
    greeting()
    player_name = run()
    print()
    print(game_name.RULES)
    counter = 0
    while counter < NUMBER_OF_ROUNDS:
        question = game_name.generate_question()
        answer = game_name.generate_question.answer
        print(question)
        user_answer = prompt.string('Your answer: ')
        if not (answer == user_answer):
            failure(user_answer, answer, player_name)
            break
        else:
            print('Correct!')
        if counter == 2:
            success(player_name)
        counter += 1
