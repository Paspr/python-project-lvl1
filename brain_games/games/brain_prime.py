import random


def greeting_prime():
    print('Answer "yes" if the given number is prime. Otherwise answer "no".')


def generate_question():
    random_number = (random.randint(1, 100),)
    generate_question.answer = correst_answer(random_number[0])
    return random_number


def correst_answer(question):
    if is_prime(question):
        return 'yes'
    else:
        return 'no'


def check_answer(question, user_answer):
    return question == user_answer


def is_prime(number):
    isprime = True
    i = 2
    if number >= 2:
        while i < number:
            if number % i == 0:
                isprime = False
            i += 1
    else:
        isprime = False
    return isprime


def prime():
    print('Answer "yes" if the given number is prime. Otherwise answer "no".')


if __name__ == '__main__':
    prime()
