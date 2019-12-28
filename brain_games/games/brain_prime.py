from brain_games.cli import run, prompt
from brain_games.engine import greeting, failure, success, wrong_input
import random

NUMBER_OF_ROUNDS = 3


def prime():
    def is_prime(number):
        isprime = True
        i = 2
        if number >= 2:
            while i < number:
                if number % i == 0:
                    isprime = False
                i += 1
        else:
            isprime = False
        return isprime
    
    greeting()
    player_name = run()
    print('Answer "yes" if the given number is prime. Otherwise answer "no".')
    print()
    counter = 0
    while counter < NUMBER_OF_ROUNDS:
        number_guess = random.randint(1, 350)
        print(f'Question: {number_guess}')
        user_answer = prompt.string('Your answer: ')
        if (is_prime(number_guess) and user_answer == 'yes') or \
                (not(is_prime(number_guess)) and user_answer == 'no'):
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
    prime()
