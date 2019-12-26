from brain_games.cli import run, prompt
import random

NUMBER_OF_ROUNDS = 3


def failure(wrong, right, name):
    print(f'"{wrong}" is a wrong answer ;(. Correct answer was "{right}"')
    print(f"Let's try again, {name}!")


def success(name):
    print(f"Congratulations, {name}!")


def wrong_input(name):
    print('Your input is incorrect')
    print(f"Let's try again, {name}!")


def even():
    player_name = main()
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

    player_name = main()
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


def gcd():
    def compute_gcd(operand_a, operand_b):
        if operand_b == 0:
            return operand_a
        else:
            return compute_gcd(operand_b, operand_a % operand_b)

    player_name = main()
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


def progression():
    player_name = main()
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

    player_name = main()
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


def main():
    print('Welcome to the Brain Games!')
    return run()


if __name__ == '__main__':
    main()
