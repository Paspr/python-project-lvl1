import random
import math


RULES = 'Answer "yes" if the given number is prime. Otherwise answer "no".'


def generate_question():
    random_number = random.randint(1, 100)
    generate_question.answer = 'yes' if is_prime(random_number) else 'no'
    return random_number


def is_prime(number):
    if number == 2:
        return True
    if number % 2 == 0 or number <= 1:
        return False
    sqr = int(math.sqrt(number)) + 1
    for divisor in range(3, sqr, 2):
        if number % divisor == 0:
            return False
    return True
