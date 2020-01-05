import random


def greeting_gcd():
    print('Find the greatest common divisor of the given numbers.')


def generate_question():
    first_operand = random.randint(1, 100)
    second_operand = random.randint(1, 100)
    generate_question.answer = compute_gcd(first_operand, second_operand)
    return first_operand, second_operand


def compute_gcd(operand_a, operand_b):
    if operand_b == 0:
        return operand_a
    else:
        return compute_gcd(operand_b, operand_a % operand_b)


def check_answer(question, user_answer):
    return question == user_answer


def gcd():
    print('Find the greatest common divisor of the given numbers.')


if __name__ == '__main__':
    gcd()
