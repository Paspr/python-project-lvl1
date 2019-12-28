def greeting():
    print('Welcome to the Brain Games!')

def failure(wrong, right, name):
    print(f'"{wrong}" is a wrong answer ;(. Correct answer was "{right}"')
    print(f"Let's try again, {name}!")


def success(name):
    print(f"Congratulations, {name}!")


def wrong_input(name):
    print('Your input is incorrect')
    print(f"Let's try again, {name}!")
