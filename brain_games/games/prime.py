import random
from math import factorial


RULES = 'Answer "yes" if the given number is prime. Otherwise answer "no".'


def generate_question():
    random_number = random.randint(1, 100)
    answer = 'yes' if is_prime(random_number) else 'no'
    return random_number, answer


def is_prime(number):
    return factorial(number - 1)  % number == number - 1
