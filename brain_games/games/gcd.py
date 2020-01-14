import random


RULES = 'Find the greatest common divisor of the given numbers.'


def generate_question():
    first_operand = random.randint(1, 100)
    second_operand = random.randint(1, 100)
    generate_question.answer = str(compute_gcd(first_operand, second_operand))
    question = f'{first_operand} {second_operand}'
    return question


def compute_gcd(operand_a, operand_b):
    if operand_b == 0:
        return operand_a
    else:
        return compute_gcd(operand_b, operand_a % operand_b)
