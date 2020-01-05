import random


def greeting_progression():
    print('What number is missing in the progression?')


def generate_question():
    length = 10
    first = random.randint(1, 25)
    position = random.randint(0, 8)
    difference = random.randint(1, 10)
    missing_number = first + (position + 1) * difference
    generate_question.answer = missing_number
    counter_progression = 0
    question = (first,)
    while counter_progression < length - 1:
        if counter_progression == position:
            question = question + ('..',)
            first += difference
        else:
            first += difference
            question = question + (first,)
        counter_progression += 1
    return question


def check_answer(question, user_answer):
    return question == user_answer


def progression():
    print('What number is missing in the progression?')


if __name__ == '__main__':
    progression()
