from brain_games.cli import run, prompt
from brain_games.engine import greeting, failure, success, wrong_input
import random

NUMBER_OF_ROUNDS = 3


def calc():
    def compute_answer(operation, operand_a, operand_b):
        answer = 0
        if operation == '*':
            answer = operand_a * operand_b
        elif operation == '+':
            answer = operand_a + operand_b
        elif operation == '-':
            answer = operand_a - operand_b
        return answer

    greeting() 
    player_name = run()
    print('What is the result of the expression?')
    print()
    operations_tuple = ('*', '-', '+')
    counter = 0
    while counter < NUMBER_OF_ROUNDS:
        current_operation = random.choice(operations_tuple)
        first_operand = random.randint(1, 100)
        second_operand = random.randint(1, 100)
        print(f'Question: {first_operand} {current_operation}'
              f' {second_operand}')
        right_answer = compute_answer(current_operation, first_operand,
                                      second_operand)
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
    calc()