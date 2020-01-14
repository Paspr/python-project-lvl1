import random


RULES = 'Answer "yes" if number is even otherwise answer "no"'


def generate_question():
    random_number = random.randint(1, 100)
    generate_question.answer = 'yes' if is_even(random_number) else 'no'
    return random_number


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
