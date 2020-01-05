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
    if game_name.__name__ == 'brain_games.games.brain_even':
        game_name.greeting_even()
    elif game_name.__name__ == 'brain_games.games.brain_calc':
        game_name.greeting_calc()
    elif game_name.__name__ == 'brain_games.games.brain_gcd':
        game_name.greeting_gcd()
    elif game_name.__name__ == 'brain_games.games.brain_progression':
        game_name.greeting_progression()
    elif game_name.__name__ == 'brain_games.games.brain_prime':
        game_name.greeting_prime()
    counter = 0
    while counter < NUMBER_OF_ROUNDS:
        question = game_name.generate_question()
        answer = str(game_name.generate_question.answer)
        for item in question:
            print(item, end=' ')
        print()
        user_answer = prompt.string('Your answer: ')
        if game_name.check_answer(answer, user_answer):
            print('Correct!')
            if counter == 2:
                success(player_name)
        else:
            failure(user_answer, answer, player_name)
            break
        counter += 1
