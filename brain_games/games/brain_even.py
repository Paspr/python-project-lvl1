import random


def greeting_even():
    print('Answer "yes" if number is even otherwise answer "no"')


def generate_question():
    random_number = (random.randint(1, 100),)
    generate_question.answer = correst_answer(random_number[0])
    return random_number


def check_answer(question, user_answer):
    return question == user_answer


def correst_answer(question):
    if question % 2 == 0:
        return 'yes'
    else:
        return 'no'


def even():
    print('Answer "yes" if number is even otherwise answer "no"')


if __name__ == '__main__':
    even()
