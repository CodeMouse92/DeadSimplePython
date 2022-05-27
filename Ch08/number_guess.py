import random


def generate_puzzle(low=1, high=100):
    print(f"I'm thinking of a number between {low} and {high}...")
    return random.randint(low, high)


def make_guess(target):
    guess = None
    while guess is None:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            print("Enter an integer.")

    if guess == target:
        return True

    if guess < target:
        print("Too low.")
    elif guess > target:
        print("Too high.")
    return False


def play(tries=8):
    target = generate_puzzle()
    while tries > 0:
        if make_guess(target):
            print("You win!")
            return
        tries -= 1
        print(f"{tries} tries left.")

    print(f"Game over! The answer was {target}.")


if __name__ == '__main__':
    play()
