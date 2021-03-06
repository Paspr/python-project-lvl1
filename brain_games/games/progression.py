import random


RULES = 'What number is missing in the progression?'


def generate_question():
    length = 10
    first = random.randint(1, 25)
    position = random.randint(0, 8)
    difference = random.randint(1, 10)
    missing_number = first + (position + 1) * difference
    answer = str(missing_number)
    counter_progression = 0
    question = f'{first}' + ' '
    while counter_progression < length - 1:
        first += difference
        if counter_progression == position:
            string_char = '..'
        else:
            string_char = str(first)
        question = question + string_char + ' '
        counter_progression += 1
    return question, answer
