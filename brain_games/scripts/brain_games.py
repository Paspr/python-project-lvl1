from brain_games.cli import run, prompt
import random


def even():
    def failure(wrong, right):
        print(f'"{wrong}" is a wrong answer ;(. Correct answer was "{right}"')
        print(f"Let's try again, {name}!")

    def success():
        print(f"Congratulations, {name}!")

    def incorrect():
        print('Your input is incorrect')
        print(f"Let's try again, {name}!")

    print('Welcome to the Brain Games!')
    print('Answer "yes" if number is even otherwise answer "no"')
    name = run()
    print()
    counter = 0
    while counter < 3:
        number_guess = random.randint(1, 100)
        print(f'Question: {number_guess}')
        user_answer = prompt.string('Your answer: ')
        if (number_guess % 2 == 0 and user_answer == 'yes') or\
                (number_guess % 2 != 0 and user_answer == 'no'):
            print('Correct!')
            if counter == 2:
                success()
        elif user_answer == 'no':
            failure('no', 'yes')
            break
        elif user_answer == 'yes':
            failure('yes', 'no')
            break
        else:
            incorrect()
            break
        counter += 1


def main():
    print('Welcome to the Brain Games!')
    run()


if __name__ == '__main__':
    main()
