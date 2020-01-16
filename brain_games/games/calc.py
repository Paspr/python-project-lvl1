import random
import operator


RULES = 'What is the result of the expression?'
OPERATIONS = (('*', operator.mul), (
        '-', operator.sub), ('+', operator.add))


def generate_question():
    operation_sign, operation_operator = random.choice(OPERATIONS)
    first_operand = random.randint(1, 100)
    second_operand = random.randint(1, 100)
    answer = str(operation_operator(
        first_operand, second_operand))
    question = f'{first_operand} {operation_sign} {second_operand}'
    return question, answer
