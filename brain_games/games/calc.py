import random
import operator


RULES = 'What is the result of the expression?'


def generate_question():
    operations_tuple = (('*', operator.mul), (
        '-', operator.sub), ('+', operator.add))
    current_operation = random.choice(operations_tuple)
    first_operand = random.randint(1, 100)
    second_operand = random.randint(1, 100)
    generate_question.answer = str(current_operation[1](
        first_operand, second_operand))
    question = f'{first_operand} {current_operation[0]} {second_operand}'
    return question
