from brain_games.cli import run, prompt

NUMBER_OF_ROUNDS = 3


def greet():
    print('Welcome to the Brain Games!')


def declare_failure(wrong, right, player_name):
    print(f'"{wrong}" is a wrong answer ;(. Correct answer was "{right}"')
    print(f"Let's try again, {player_name}!")


def congratulate(player_name):
    print(f"Congratulations, {player_name}!")


def run_game(game_name):
    greet()
    player_name = run()
    print()
    print(game_name.RULES)
    counter = 0
    while counter < NUMBER_OF_ROUNDS:
        question, answer = game_name.generate_question()
        print(question)
        user_answer = prompt.string('Your answer: ')
        if not answer == user_answer:
            declare_failure(user_answer, answer, player_name)
            break
        print('Correct!')
        counter += 1
    else:
        congratulate(player_name)
