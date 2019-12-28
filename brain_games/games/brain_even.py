from brain_games.cli import run, prompt
from brain_games.engine import greeting, failure, success, wrong_input
import random

NUMBER_OF_ROUNDS = 3


def even():
    greeting()
    player_name = run()
    print('Answer "yes" if number is even otherwise answer "no"')
    print()
    counter = 0
    while counter < NUMBER_OF_ROUNDS:
        number_guess = random.randint(1, 100)
        print(f'Question: {number_guess}')
        user_answer = prompt.string('Your answer: ')
        if (number_guess % 2 == 0 and user_answer == 'yes') or \
                (number_guess % 2 != 0 and user_answer == 'no'):
            print('Correct!')
            if counter == 2:
                success(player_name)
        elif user_answer == 'no':
            failure('no', 'yes', player_name)
            break
        elif user_answer == 'yes':
            failure('yes', 'no', player_name)
            break
        else:
            wrong_input(player_name)
            break
        counter += 1


if __name__ == '__main__':
    even()
