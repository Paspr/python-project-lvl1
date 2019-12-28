from brain_games.cli import run, prompt
from brain_games.engine import greeting, failure, success
import random

NUMBER_OF_ROUNDS = 3


def progression():
    greeting()
    player_name = run()
    print('What number is missing in the progression?')
    print()
    length = 10
    counter = 0
    while counter < NUMBER_OF_ROUNDS:
        first = random.randint(1, 25)
        position = random.randint(0, 8)
        difference = random.randint(1, 10)
        missing_number = first + (position + 1) * difference
        counter_progression = 0
        print(first, end=' ')
        while counter_progression < length - 1:
            if counter_progression == position:
                print('..', end=' ')
                first += difference
            else:
                first += difference
                print(first, end=' ')
            counter_progression += 1
        print()
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(missing_number):
            print('Correct!')
            if counter == 2:
                success(player_name)
        else:
            failure(user_answer, missing_number, player_name)
            break
        counter += 1


if __name__ == '__main__':
    progression()
