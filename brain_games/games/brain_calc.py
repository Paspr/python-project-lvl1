import random


def generate_question():
    operations_tuple = ('*', '-', '+')
    current_operation = random.choice(operations_tuple)
    first_operand = random.randint(1, 100)
    second_operand = random.randint(1, 100)
    generate_question.answer = compute_answer(
        current_operation, first_operand, second_operand
        )
    return first_operand, current_operation, second_operand


def compute_answer(operation, operand_a, operand_b):
    answer = 0
    if operation == '*':
        answer = operand_a * operand_b
    elif operation == '+':
        answer = operand_a + operand_b
    elif operation == '-':
        answer = operand_a - operand_b
    return answer


def check_answer(question, user_answer):
    return question == user_answer


def greeting_calc():
    print('What is the result of the expression?')


def calc():
    print('What is the result of the expression?')


if __name__ == '__main__':
    calc()
