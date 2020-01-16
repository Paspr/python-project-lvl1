import random


RULES = 'Answer "yes" if number is even otherwise answer "no"'


def generate_question():
    random_number = random.randint(1, 100)
    answer = 'yes' if is_even(random_number) else 'no'
    return random_number, answer


def is_even(number):
    return number % 2 == 0
