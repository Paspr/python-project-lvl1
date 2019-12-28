from brain_games.cli import run, prompt
from brain_games.engine import greeting, failure, success, wrong_input
import random

NUMBER_OF_ROUNDS = 3


def gcd():
    def compute_gcd(operand_a, operand_b):
        if operand_b == 0:
            return operand_a
        else:
            return compute_gcd(operand_b, operand_a % operand_b)
    greeting()
    player_name = run()
    print('Find the greatest common divisor of the given numbers.')
    print()
    counter = 0
    while counter < NUMBER_OF_ROUNDS:
        first_operand = random.randint(1, 100)
        second_operand = random.randint(1, 100)
        print(f'Question: {first_operand} {second_operand}')
        right_answer = compute_gcd(first_operand, second_operand)
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(right_answer):
            print('Correct!')
            if counter == 2:
                success(player_name)
        else:
            failure(user_answer, right_answer, player_name)
            break
        counter += 1


if __name__ == '__main__':
    gcd()
